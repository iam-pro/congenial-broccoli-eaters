import ctypes

so = ctypes.cdll.LoadLibrary('./something.so')
do = so.run
do()