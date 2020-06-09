class Analyser(object):
    def __init__(self, fs, cutting_speed):
        self.fs = fs
        self.cutting_speed = cutting_speed

    def process_scanner(self, data):
        import numpy as np

        # Specify cutting duration according to applied cutting speed and sampling rate
        cutting_duration = int(0.1*self.fs/self.cutting_speed)

        # Find a window corresponding to the cutting process
        values = []
        for i in range(0, len(data)):
            try:
                value = np.mean(data[i:i+cutting_duration])
                values.append(value)
            except Exception as e: # in case if i + cutting_duration > len(data)
                print(e)

        start = values.index(max(values))
        finish = start + cutting_duration

        return start, finish

    def peak_analyser(self, data):
        import itertools
        import math
        import numpy as np
        from scipy.signal import find_peaks

        # Find start and finish points
        start, finish = self.process_scanner(data)
        data = data[start:finish]

        # Find peaks
        rmsValue = np.sqrt(np.mean(data**2))
        peaksHD, _ = find_peaks(data, height=rmsValue, distance=10)
        peaksHD = peaksHD + start

        return peaksHD