import os,time,platform
os.system('clear')
os.system('git pull')
#print('\033[1;92m[>] Checking Updates')
#os.system('pip install requests mechanize bs4 rich')#
os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
    import MH64
elif bit=='32bit':
    import MH32
