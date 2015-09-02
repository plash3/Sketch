from os import getcwd
from os import listdir
from os import chdir
from os import rename

def mv_files():
    chdir('/media/paul/DATA/AUDIO/Franklin_Autobio')
    d = getcwd()
    print "PWD:", d
    files = listdir(d)
    for file in files:
        newfile = file.replace('_pine_64kb', '').capitalize()
        rename(file, newfile)
        print file, newfile

mv_files()
