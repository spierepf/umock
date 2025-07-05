import os
import sys

libpath = 'lib'
sys.path.insert(0, libpath)
if libpath not in os.listdir():
    os.mkdir(libpath)
