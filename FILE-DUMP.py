import os
from platform import architecture
if architecture()[0]=='64bit':os.system('git pull;chmod +x MAHADI;./MAHADI')
else:exit('\033[1;31m\n Sorry 32bit device not support ')
