import os
import platform
os.system('xdg-open https://github.com/MAHADI-143')
b = platform.architecture()[0]
if b == '64bit':
    import DUMP
elif b == '32bit':
    print("32bit Not Supported! Sorry")
