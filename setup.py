import cx_Freeze
import sys
import pandas
import numpy
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\oguz.sarigul\AppData\Local\Continuum\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\oguz.sarigul\AppData\Local\Continuum\Anaconda3\tcl\tk8.6'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [cx_Freeze.Executable("GUI.py", base=base)]

cx_Freeze.setup(name='PRproject',
                options={"build_exe": {"packages": ["tkinter", "pandas", "numpy"],
                                       "include_files": ["proptable.csv", "compounds.csv", "logo.ico",
                                                         r"C:\Users\oguz.sarigul\AppData\Local\Continuum\Anaconda3\DLLs\tcl86t.dll",
                                                         r"C:\Users\oguz.sarigul\AppData\Local\Continuum\Anaconda3\DLLs\tk86t.dll"]}},
                version='0.1',
                description="Program implements Peng Robinson Method (1974 article),"
                            " using DDBST Online Databank (http://www.ddbst.com/)",
                executables= executables)

