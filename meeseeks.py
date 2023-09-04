import re

def changeIndex(l,y,i):
    action = locals().get('y')

    if (action == 'bond') or (action == 'pair'):
        for j in range(2,5,2):
            if int(l[j]) > index[i]:
                l[j] = str(int(l[j]) - 1)
        return ''.join(l)
    elif (action == 'angle'):
        for j in range(2,7,2):
            if int(l[j]) > index[i]:
                l[j] = str(int(l[j]) - 1)
        return ''.join(l)
    elif (action == 'dihedral'):
        for j in range(2,9,2):
            if int(l[j]) > index[i]:
                l[j] = str(int(l[j]) - 1)
        return ''.join(l)


def removeBonds():
    for i in range(len(index)):
        tmp = []
        for n,line in enumerate(bond[-1]):
            l = re.split(r'(\s+)', line)
            if i < len(index):
                if (index[i] > int(l[2])) and (index[i] > int(l[4])):
                    tmp.append(line)
                elif ' '+str(index[i])+' ' in line:
                    continue
                else:
                    tmp.append(changeIndex(l,'bond',i))
                #else:
                    #print(l)
            else:
                continue
        index[i:] = [ind - 1 for ind in index[i:]]
        bond.append(tmp)

    writeOut('Bonds', bond)

def removePairs():
    for i in range(len(index)):
        tmp = []
        for n,line in enumerate(pair[-1]):
            l = re.split(r'(\s+)', line)
            if i < len(index):
                if (index[i] > int(l[2])) and (index[i] > int(l[4])):
                    tmp.append(line)
                elif ' '+str(index[i])+' ' in line:
                    continue
                else:
                    tmp.append(changeIndex(l,'pair',i))
                #else:
                    #print(l)
            else:
                continue
        index[i:] = [ind - 1 for ind in index[i:]]
        pair.append(tmp)

    writeOut('Pairs', pair)

def removeAngles():
    for i in range(len(index)):
        tmp = []
        for n,line in enumerate(angle[-1]):
            l = re.split(r'(\s+)', line)
            if i < len(index):
                if (index[i] > int(l[2])) and (index[i] > int(l[4])) and (index[i] > int(l[6])):
                    tmp.append(line)
                elif ' '+str(index[i])+' ' in line:
                    continue
                else:
                    tmp.append(changeIndex(l,'angle',i))
                #else:
                    #print(l)
            else:
                continue
        index[i:] = [ind - 1 for ind in index[i:]]
        angle.append(tmp)

    writeOut('Angles', angle)

def removeDihedral():
    for i in range(len(index)):
        tmp = []
        for n,line in enumerate(dihedral[-1]):
            l = re.split(r'(\s+)', line)
            if i < len(index):
                if (index[i] > int(l[2])) and (index[i] > int(l[4])) and (index[i] > int(l[6])) and (index[i] > int(l[8])):
                    tmp.append(line)
                elif ' '+str(index[i])+' ' in line:
                    continue
                else:
                    tmp.append(changeIndex(l,'dihedral',i))
                #else:
                    #print(l)
            else:
                continue
        index[i:] = [ind - 1 for ind in index[i:]]
        dihedral.append(tmp)

    writeOut('Dihedral', dihedral)

def writeOut(command, x):
    command = locals().get('command')
    with open('topol.txt', 'a') as file:
        file.write(f'[{command}]\n')
        for line in x[-1]:
            file.write(line)
###################################################
# main program
ind = open('index.txt', 'r').read().splitlines()
index = []
for i in range(len(ind)):
    index.append(int(ind[i]))
index = sorted(index)
indexBackup = 1 * index


bondInfo = open('bonds.txt', 'r').readlines()
bond = [bondInfo] * 1

pairInfo = open('pairs.txt', 'r').readlines()
pair = [pairInfo] * 1

angleInfo = open('angle.txt', 'r').readlines()
angle = [angleInfo] * 1

dihedralInfo = open('dihedral.txt', 'r').readlines()
dihedral = [dihedralInfo] * 1

removeBonds()
index = 1 * indexBackup
removePairs()
index = 1 * indexBackup
removeAngles()
index = 1 * indexBackup
removeDihedral()

