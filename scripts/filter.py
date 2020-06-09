class Filter(object):
    def __init__(self, fs):
        self.fs = fs
        
    def butter_lowpass(self, cut_off=10000, order=5):
        from scipy.signal import butter

        nyq = 0.5 * self.fs
        normal_cutoff = cut_off / nyq
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        
        return b, a
    
    def butter_lowpass_filter(self, data, order=5):
        from scipy.signal import lfilter

        b, a = self.butter_lowpass(order=order)
        y = lfilter(b, a, data)
        
        return y
    
    def build_inverse_matrix(self):
        import numpy as np

        # Imports for Y-axis
        Y_response = np.loadtxt('components\\impact_test.txt', delimiter=',')[:, 1] # channel 1
        Y_applied = np.loadtxt('components\\impact_test.txt', delimiter=',')[:, 3] # channel 3

        # Fast Fourier transform (filter components)
        Y_response = np.fft.fft(Y_response, n=None, axis=-1, norm=None)
        Y_applied = np.fft.fft(Y_applied, n=None, axis=-1, norm=None)

        # Build transfer matrices
        HYY = Y_applied / Y_response

        return HYY

    def offset(self, data, channel_y):
        import numpy as np

        # Mean value out of 10 000 first samples
        offset_Y = np.mean(data[0:len(data), channel_y])

        if offset_Y > 0:
            data[:, channel_y] = data[:, channel_y] - offset_Y
        else:
            data[:, channel_y] = data[:, channel_y] + offset_Y 

        return data

    def transform(self, path, H_YY, channel_y, cutting_speed):
        import numpy as np
        from . import analyser
        from scipy.signal import hilbert
        
        # Import and perform basic operations (e.g. offset correction)
        data = -np.loadtxt(path, delimiter=',')
        data = self.offset(data, channel_y)
        
        # Perform peak analysis
        analyser_ = analyser.Analyser(fs=self.fs, cutting_speed=cutting_speed)
        start, _ = analyser_.process_scanner(data=data)

        # Crop to size
        if len(data) != 100000:
            data = data[start-10000:start+90000, channel_y]
        else:
            data = data[:, channel_y]

        # Filter (measurement data)
        data_y = self.butter_lowpass_filter(data)

        # Fast Fourier transform (measurement data)
        data_y = np.fft.fft(data_y, n=None, axis=-1, norm=None)

        # Inverse filtering of uploaded data
        data_y_corrected = (H_YY * data_y)
        data_y_corrected = np.fft.ifft(data_y_corrected, n=None, axis=-1, norm=None)
        data_y_corrected = data_y_corrected.real * (-1)

        # Signal envelope
        analytic_signal_Y = hilbert(data_y_corrected)
        data_y_corrected_envelope = np.abs(analytic_signal_Y)

        '''
        a1 - original signal in Y-axis
        b1 - corrected signal in Y-axis
        c1 - envelope of corrected signal in Y-axis
        '''
        a1 = data
        b1 = data_y_corrected
        c1 = data_y_corrected_envelope
        
        return a1, b1, c1