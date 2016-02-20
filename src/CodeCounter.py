'''
Created on 13.01.2016

@author: Admin
'''

import argparse
import statistics
import os

parser = argparse.ArgumentParser(description='This tool counts line of all files found recursively')
parser.add_argument('-s','--skipfolders',help='while searching skip -s folder1 folder2 folder3', nargs='+', required=False, default = [""])
parser.add_argument('-f','--filetypes',help='only search files ending with -f .txt .class .py', nargs='+', required=False, default = [""])
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
    readable,unreadable = [],[] 

    for filename in filelist:
        zeilen = 0
        try:
            with open(filename) as file:
                for l in file.readlines():
                    if len(l.strip()) > 0:
                        zeilen +=1
        except:
            zeilen = -1
        if zeilen == -1:
            unreadable.append([zeilen,filename])
        else:
            readable.append([zeilen,filename])
        
    readable.sort(key=lambda x: x[0])
    return readable,unreadable

def findFiles(skipfolders,filetype,minsize,maxsize):
    
    filelist = []
    for path,folders,files in os.walk('.',topdown=True):
        if not any(path.endswith(f) for f in skipfolders): ############################# naice
            for file in [x for x in files if x.endswith(tuple(filetype)) if os.path.getsize(os.path.join(path, x)) >= minsize]: 
                if not maxsize or os.path.getsize(os.path.join(path, file)) <= maxsize: ############################# remember?
                    ### hier möchte mute continue if verwenden
                    filelist.append(os.path.join(path, file))
            
    printStats(*countLines(filelist))



def printStats(readable,unreadable):
    print(len(readable),"READABLE files found!")
    print(len(unreadable),"UNREADABLE files found!")
    if len(readable) > 2:
        print(round(statistics.mean([x[0] for x in readable]),2),"lines is avg!")
        print(statistics.median([x[0] for x in readable]),"lines is median")
        print()
        print("--- Start Top5 ---")
        print("Linecount - Filename")
        for x in range(1,6):
            print(readable[len(readable)-x][0],"  -  ",readable[len(readable)-x][1])
        print("--- Stop Top5 ---")
        print()
        print("--- Start Low5 ---")
        print("Linecount - Filename")
        for x in range(5):
            print(readable[x][0],"  -  ",readable[x][1])
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