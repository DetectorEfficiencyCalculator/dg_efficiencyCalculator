"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

import macholib
#print("~"*60 + "macholib verion: "+macholib.__version__)
if macholib.__version__ <= "1.7":
    print("Applying macholib patch...")
    import macholib.dyld
    import macholib.MachOGraph
    dyld_find_1_7 = macholib.dyld.dyld_find
    def dyld_find(name, loader=None, **kwargs):
        #print("~"*60 + "calling alternate dyld_find")
        if loader is not None:
            kwargs['loader_path'] = loader
        return dyld_find_1_7(name, **kwargs)
    macholib.MachOGraph.dyld_find = dyld_find

APP = ['launch.py']
DATA_FILES = []
OPTIONS = {
          #'bdist_base': str(Path(getcwd()).parent)+'/build', 'dist_dir': str(Path(getcwd()).parent) + '/dist',
    'argv_emulation': True, 'includes': ['sip', 'PyQt5._qt'],
    #'plist': { 'PyRuntimeLocations': ['/Library/Frameworks/Python.framework/Versions/3.6/Python',]}
    }

setup(
    name='EffCalculator',
    version="0.0.2",
    app=APP,
    author='Alvaro Carmona',
    author_email='acarmona@opendeusto.es',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    license="BSD",
    setup_requires=['py2app'],
    packages=['efficiencyCalculator'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],

)
