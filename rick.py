import re

#list of atoms to be changed

#N1 = {
    #'kind'='',
    #'atom'='',
    #'charge'='',
    #'mass'='',
    #'qtot'=''}

def listOldAtoms():
    #read database of parameters
    with open('atomsToBeReplaced.txt', 'r') as f2:
       return f2.readlines()

def listNewAtoms():
    with open('newAtoms.txt', 'r') as f3:
       return f3.readlines()

#build dictionaries
def makeDict():
    for n,line in enumerate(oldAtoms):
        l = re.split(r'(\s+)', line)
        dictyOld = {n:{
            'kind': l[4],
            'atom': l[10]+' ',
            'charge': l[14],
            'mass': l[16],
            'qtot': l[22]
            }}
        atomsToBeReplaced.append(dictyOld)

    for n,line in enumerate(newAtoms):
        l = re.split(r'(\s+)', line)
        dictyNew = {n:{
            'kind': l[4],
            'atom': l[10],
            'charge': l[14],
            'mass': l[16],
            'qtot': l[22]
            }}
        atomsToMoveIn.append(dictyNew)

#change parameters
def changeParameters(i,l):
    #type
    l[4] = atomsToMoveIn[i][i]['kind']
    #atom
    l[10] = atomsToMoveIn[i][i]['atom']
    #charge
    l[14] = atomsToMoveIn[i][i]['charge']
    #mass
    l[16] = atomsToMoveIn[i][i]['mass']
    #qtot
    l[22] = atomsToMoveIn[i][i]['qtot']
    return ''.join(l)

#find atom and replace
def replaceAtoms():
    for i in range(len(atomsToMoveIn)):
        tmp = []
        for n,line in enumerate(output[-1]):
            l = re.split(r'(\s+)', line)
            if ('VIPR' in line and atomsToBeReplaced[i][i]['atom'] in line) or ('VIPS' in line and atomsToBeReplaced[i][i]['atom'] in line):
                #if atomsToBeReplaced[i]['atom'] in line:
                tmp.append(changeParameters(i,l))
            else:
                tmp.append(line)
        #print(tmp)
        output.append(tmp)

def writeOut():
    with open('newItp2.txt', 'w') as file:
        for line in output[-1]:
            file.write(line)
    #code from morty

######################################################################

#main program
with open('newItp.txt', 'r') as f:
    fileData = f.readlines()

#create dictionaries
atomsToBeReplaced = [] #atoms to be replaced from old itp
atomsToMoveIn = [] #atoms that must replace old atoms

oldAtoms = listOldAtoms()
newAtoms = listNewAtoms()
makeDict()
output = [fileData] * 1
replaceAtoms()
writeOut()

# modificar interação do hidrogenio H61 pra ligar no carbono que substitui o nitrogenio
