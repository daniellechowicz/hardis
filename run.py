import argparse
import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='Inverse filtering in cutting force analysis by Daniel Lechowicz')

# Add the arguments
my_parser.add_argument('-p',
                       '--path',
                       dest='path',
                       type=str,
                       required=True,
                       help="Enter the path to the file folder")
my_parser.add_argument('-ch',
                       '--channel',
                       dest='channel',
                       type=int,
                       required=True,
                       help='Enter the channel number corresponding to the Y axis')
my_parser.add_argument('-fs',
                       '--sampling_rate',
                       dest='sampling_rate',
                       type=int,
                       required=True,
                       help='Enter the sampling rate used')

# Execute the parse_args() method
args = my_parser.parse_args()

def main():
    import numpy as np
    import os
    from scripts import analyser, filter, plotter, tools
    from xlwt import Workbook

    # Initialize classes
    # Filter class
    filter_ = filter.Filter(fs=args.sampling_rate)
    # Plotter class
    plotter_ = plotter.Plotter()
    # Workbook class 
    wb = Workbook()

    # Before any calculations, two inverse matrices need to be prepared (X and Y)
    H_YY = filter_.build_inverse_matrix()

    # Create an Excel sheet
    sheet = wb.add_sheet('results')

    # Get all the files within your directory
    folder_path = args.path
    files_ = os.listdir(folder_path)

    # Filter "files_" to find files with the ending ".txt"
    files = []
    for file in files_:
        if file.endswith('.txt'):
            files.append(file)
        else:
            continue
    
    for i, filename in enumerate(files):
        # Get cutting speed (based on its filename)
        cutting_speed = int(filename[-6:-4])

        # Specify the path
        path = os.path.join(folder_path, filename)

        # Get the transformed data from the "Filter" class
        a1, b1, c1 = filter_.transform(path=path, H_YY=H_YY, channel_y=args.channel, cutting_speed=cutting_speed)

        # Resultant cutting force
        data_original = a1
        data_corrected = b1

        # Perform peak analysis
        analyser_ = analyser.Analyser(fs=args.sampling_rate, cutting_speed=cutting_speed)
        chosen_peaks_values = analyser_.peak_analyser(data=data_corrected)

        # Plot (entire file)
        plotter_.plot_v1(filename=filename,
                         chosen_peaks_values=chosen_peaks_values,
                         data_original=data_original,
                         data_corrected=data_corrected)
        
        # Plot (zoom into cutting range)
        plotter_.plot_v2(filename=filename,
                         chosen_peaks_values=chosen_peaks_values,
                         data_original=data_original,
                         data_corrected=data_corrected)

        # Save to ".xls" file
        data_package = [filename,
                        np.mean(data_corrected[chosen_peaks_values]),
                        np.median(data_corrected[chosen_peaks_values]),
                        np.std(data_corrected[chosen_peaks_values]),
                        max(data_corrected[chosen_peaks_values])]
        tools.save_to_excel(workbook=wb, sheet=sheet, row=i+1, data=data_package)

        # Keep user updated about current progress
        print('[INFO] file ► {} ◄ has been processed'.format(filename[:-4]))
        
if __name__ == "__main__":
    main()