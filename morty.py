#script to remove atoms from itp

import re #c = re.split(r'(\s+)', fileData[n])

def takeIndex(x,fileData):
    n = 0
    for i in range(len(fileData)):
        if x in fileData[n]:
            index.append(n+1)
            with open('index.txt', 'a') as fout:
                fout.write(f'{n+1}'+'\n')
        n += 1


def stealThere(julia):
    # remove atoms
    for i in range(len(index)):
        tmp = []
        for n,line in enumerate(output[-1]):
            l = re.split(r'(\s+)', line)
            print(l)
            if i < len(index):
                if index[i] > int(l[2]):
                    tmp.append(line)
                elif index[i] < int(l[2]):
                    tmp.append(changeIndex(l,n))

            else:
                continue
        index[i:] = [ind - 1 for ind in index[i:]]
        output.append(tmp)

def changeIndex(l,n):
            l[2] = str(int(l[2]) - 1)
            l[12] = str(int(l[12]) - 1) #for itp
            return ''.join(l)


def writeThere():
    with open('newItp.txt', 'w') as file: #itp
    #with open('newPBC.pdb', 'w') as file: #pbc
        for line in output[-1]:
            file.write(line)



# coisar os trem
# read file
with open('itp.txt', 'r') as file: #itp
    fileData = file.readlines()
#with open('PVPmodified.pdb', 'r') as file: #pbc
    #fileData = file.readlines()[2:-1]

output = [fileData] * 1 #empty   list for files to be outputed
index = [] #empty list for index of removed atoms
atomsToBeRemoved = ['H41', 'H42']

for i in range(len(atomsToBeRemoved)):
    a = atomsToBeRemoved[i]
    takeIndex(a,fileData)
index = sorted(index)
stealThere(output)
writeThere()

