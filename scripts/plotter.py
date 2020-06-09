class Plotter(object):
    def plot_v1(self, filename, chosen_peaks_values, data_original, data_corrected):
        import matplotlib.pyplot as plt
        import numpy as np
        import os
        
        # Time and/or y-axis matrix
        t = np.linspace(0, len(data_corrected), len(data_corrected))

        textstr = '\n'.join((r'$\mathrm{mean}=%.2f$ N' % (np.mean(data_corrected[chosen_peaks_values])), 
                             r'$\mathrm{median}=%.2f$ N' % (np.median(data_corrected[chosen_peaks_values])), 
                             r'$\mathrm{std}=%.2f$ N' % (np.std(data_corrected[chosen_peaks_values])),
                             r'$\mathrm{max}=%.2f$ N' % (max(data_corrected[chosen_peaks_values]))))

        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(t, data_original, linewidth=0.5, color='dodgerblue', alpha=0.5)
        ax.plot(t, data_corrected, linewidth=0.5, color='red', alpha=1.0)
        ax.scatter(chosen_peaks_values, data_corrected[chosen_peaks_values], marker='v', color='dodgerblue', alpha=0.75)
        ax.set_xlabel('Sample [-]')
        ax.set_ylabel('Cutting force [N]')
        ax.legend(['Unfiltered', 'Filtered', 'Peak'], loc='upper right')
        ax.text(0.025, 0.95, textstr, transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=props)
    
        # Create a directory where data will be stored
        try:
            os.mkdir('.\\data')
        except:
            pass
        
        # Create a directory where figures will be stored
        try:
            os.mkdir(os.path.join('data', 'figures'))
        except:
            pass

        # Save figure
        plt.savefig(os.path.join('.\\data\\figures', filename[:-4] + '.png'))

        # Close figure (figures created through the pyplot interface may consume too much memory
        plt.close()

    def plot_v2(self, filename, chosen_peaks_values, data_original, data_corrected):
        import matplotlib.pyplot as plt
        import numpy as np
        import os
        
        # Time and/or y-axis matrix
        t = np.linspace(0, len(data_corrected), len(data_corrected))

        textstr = '\n'.join((r'$\mathrm{mean}=%.2f$ N' % (np.mean(data_corrected[chosen_peaks_values])), 
                             r'$\mathrm{median}=%.2f$ N' % (np.median(data_corrected[chosen_peaks_values])), 
                             r'$\mathrm{std}=%.2f$ N' % (np.std(data_corrected[chosen_peaks_values])),
                             r'$\mathrm{max}=%.2f$ N' % (max(data_corrected[chosen_peaks_values]))))

        props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

        show_from = chosen_peaks_values[0] - 1000
        show_to = chosen_peaks_values[-1] + 1000

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(t, data_original, linewidth=0.5, color='dodgerblue', alpha=0.5)
        ax.plot(t, data_corrected, linewidth=0.5, color='red', alpha=1.0)
        ax.scatter(chosen_peaks_values, data_corrected[chosen_peaks_values], marker='v', color='dodgerblue', alpha=0.75)
        ax.set_xlabel('Sample [-]')
        ax.set_ylabel('Cutting force [N]')
        ax.set_xlim(show_from, show_to)
        ax.legend(['Unfiltered', 'Filtered', 'Peak'], loc='upper right')
        ax.text(0.025, 0.95, textstr, transform=ax.transAxes, fontsize=10, verticalalignment='top', bbox=props)

        # Create a directory where data will be stored
        try:
            os.mkdir('.\\data')
        except:
            pass
        
        # Create a directory where figures will be stored
        try:
            os.mkdir(os.path.join('.\\data', 'figures'))
        except:
            pass
        
        # Save figure
        plt.savefig(os.path.join('.\\data\\figures', filename[:-4] + '_zoom.png'))

        # Close figure (figures created through the pyplot interface may consume too much memory
        plt.close()