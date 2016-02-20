'''
Created on 13.01.2016

@author: Admin
'''

import argparse
import statistics
import os

parser = argparse.ArgumentParser(description='This tool counts line of all files found recursively')
parser.add_argument('-s','--skipfolders',help='while searching skip all folders in ["list"]', required=False, default = [""])
parser.add_argument('-f','--filetypes',help='only search files ending with extensions in ["list"]', required=False, default = [""])
parser.add_argument('-i','--minsize',help='in filesize in bytes', type=int, required=False, default = 0)
parser.add_argument('-a','--maxsize', help='max filesize in bytes', type=int ,required=False, default = 0)
args = parser.parse_args()

print("Working with settings(to adjust see -h)...")
print("List of folder to skip: ",args.skipfolders)
print("List of file ext to search: ",args.filetypes)
print("Files with min size of (default = 0): ",args.minsize)
print("Files with max size of (default = 0): ",args.maxsize)
print()

def countLines(filelist):
    topz = []
    fails = []
    for x in range(len(filelist)):
        zeilen = 0
        try:
            for l in open(filelist[x]).readlines():
                if len(l.strip()) > 0:
                    zeilen +=1
            topz.append([zeilen,filelist[x]])
        except:
            fails.append([-1,filelist[x]])
            pass
    return([sorted(topz, key=lambda x: x[0]),fails])

def findFiles(filetype,skipfolders,minsize,maxsize):
    filelist = []
    for path,folders,files in os.walk('.',topdown=True):
        for f in skipfolders:                                               # skipping folders
            if f in folders:
                folders.remove(f) 
        for file in files:
            if file.endswith(tuple(filetype)):                              # skipping files
                if os.path.getsize(os.path.join(path, file)) >= minsize:    # checking filesizes
                    if maxsize > 0:
                        if os.path.getsize(os.path.join(path, file)) <= maxsize:
                            filelist.append(os.path.join(path, file))
                    else:
                        filelist.append(os.path.join(path, file))

    gehtbesser = countLines(filelist)
    printStats(gehtbesser[0], gehtbesser[1])
    
def printStats(topz,fails):
    print(len(topz),"READABLE files found!")
    print(len(fails),"UNREADABLE files found!")
    if len(topz) > 2:
        print(round(statistics.mean([x[0] for x in topz]),2),"lines is avg!")
        print(statistics.median([x[0] for x in topz]),"lines is median")
        print()
        print("--- Start Top5 ---")
        print("Linecount - Filename")
        for x in range(1,6):
            print(topz[len(topz)-x][0],"  -  ",topz[len(topz)-x][1])
        print("--- Stop Top5 ---")
        print()
        print("--- Start Low5 ---")
        print("Linecount - Filename")
        for x in range(5):
            print(topz[x][0],"  -  ",topz[x][1])
        print("--- Stop Low5 ---")
    else:
        print("Not enough data for further statistics :(")
    
findFiles(args.skipfolders,args.filetypes,args.minsize,args.maxsize)
''' Thoughts:
1. findFiles Argumente ubergeben oder soll sich die Funktion die Dinger selber holen uber args.XXXX?
2. Alles in eine Klasse packen, die Methoden rufen sich gehenseitig auf, arbeiten aber all an einer Klassen?variable,
ubergeben sich also keine Sachen hin und her mehr.
3. Skipfolders nur in . oder auch in subfolderns?
4. Funktioniert alles, aber iwie alles dirty in der Umsetzung

'''