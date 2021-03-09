[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

Detector Efficiency Calculator
============

Python standalone application 
This is a project in the ESS ERIC in order to make available to the public a library, a GUI tool and a webpage using Francesco Piscitelli's analytical tools for the calculation of efficiency for detectors based on solid converters.

- Webapp:          https://detectorefficiencycalculator.herokuapp.com/
- Repo:            https://github.com/DetectorEfficiencyCalculator/dg_efficiencyCalculator
- Calculation libraries: https://github.com/alvcarmona/neutronDetectorEffFunctions

Requisites
------------
- Python3: I recommend using a virtual environment  https://virtualenv.pypa.io/en/stable/userguide/
- Qt5: You can find the installation instructions here http://doc.qt.io/qt-5/ 

Installation and execution (Make sure to use python 3)
------------

Clone the repository:
```
git clone https://github.com/DetectorEfficiencyCalculator/dg_efficiencyCalculator
cd dg_efficiencyCalculator
```
Install dependencies:

```
pip install -r requirements.txt
```
You may encounter problems depending on which OS and Python version you are using when installing PyQt5, if this happens, you should install sip pyqt5 manually pointing to the desired python in your machine.

Run launch script:
```
python launch.py
```
Troubleshooting
------------

You may encounter problems depending on the OS and python when installing pyqt5, if this happens, you should install
sip pyqt5 manually for the desired python in your machine.

There are known problems with matplotlib's backend in Mac Os X (ImportError: Gtk*).
To solve this you should edit the file ".matplotlib/matplotlibrc" (Create it if it doesn't exist) and add the line "backend: TkAgg"

If you are missing the tk package:  ```sudo apt-get install python3-tk```

Developed by Álvaro Carmona Básañez

File structure
------------

```
efficiencyCalculator/       
    exports/  # examples of detector configuration files  
        waves/  
            2gaussdistr.txt  
        Detector 118effVsDepth.txt   
        Detector 11effVsDepth.txt  
        PolicromPolidconfig.json  
        detector1.json
    tests/  
        B10_test.py   
        Detector_test.py  
    detectorDialog.py  # Implementation of the window that is used to configure and optimize detectors  
    detectorDialogTab.ui # Qt UI file  
    detectorform.ui     # Qt UI file  
    efficiencyCalculator.py  # implementation of the first window, lists detector configurations  
    efficiencyMainwindow.ui  
    efficiencyMainwindow2.ui     
.gitignore    
.hgignore  
LICENSE  
README.txt  
launch.py   # Script to launch GUI application  
launch.spec  
requirements.txt  # Pip dependencies  
setup.py  # Packaging information  
```