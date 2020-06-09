# Inverse filtering in cutting force analysis
Applied detailed cutting force analysis based on Girardin, F., et al. (2010): *High Frequency Correction of Dynamometer for Cutting Force Observation in Milling*  in *Journal of Manufacturing Science and Engineering* 132(3)

## How to set up the software?
1. Go to https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe

<p align="center"> 
<img src="https://github.com/daniellechowicz/cutting-force-analysis-web/blob/master/src/instruction/1.PNG">
</p>

2. Install the downloaded file (which is a Python interpreter) and make sure **Add Python 3.7 to PATH** is checked

<p align="center"> 
<img src="https://github.com/daniellechowicz/cutting-force-analysis-web/blob/master/src/instruction/2.PNG">
</p>

3. When the installation is complete, press **Close**

<p align="center"> 
<img src="https://github.com/daniellechowicz/cutting-force-analysis-web/blob/master/src/instruction/6.png">
</p>

4. Clone or download the content of the repository
5. Extract **cutting-force-analysis-web-master.zip** and open the folder

## Issues related to data acquisition and file format
1. As the modal tests were performed at a sampling rate of 100 000 Hz, the sampling rate of the measurement files must be the same (i.e. 100 000 Hz)
2. The format of the measurement files must be **.txt**
3. Columns must be separated with semicolons
4. Nor headers neither comments are allowed
5. Before running the software, you will be requested to enter the column number (remember that the numbering in Python starts with 0)

## What needs to be done?
The software was adapted to the test setup designed by *Kompetenzzentrum Holz GmbH*. In order for the software to function properly, it is necessary to carry out modal tests of the test setup with the relevant parameters as specified in the "Issues related to data acquisition and file format" section. Depending on your interest in further development of the application, an upgrade of this software will be carried out.
