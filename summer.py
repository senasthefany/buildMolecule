# change atoms in pbc
with open('newPBC.pdb', 'r') as file:
    fileData = file.readlines()[2:-1]

atomsToBeReplaced = ['C6  VIPR','H21 VIPR','N1  VIPR','C3  VIPR','O1  VIPR','C4  VIPR','C2  VIPR','H61 VIPR','H62 VIPR','C5  VIPR','H51 VIPR','H52 VIPR','C6  VIPS','H21 VIPS','N1  VIPS','C3  VIPS','O1  VIPS','C4  VIPS','C2  VIPS','H61 VIPS','H62 VIPS','C5  VIPS','H51 VIPS','H52 VIPS']
atomsToMoveIn = ['C19 VIPR','H7  VIPR','C18 VIPR','C21 VIPR','O3  VIPR','O1  VIPR','C6  VIPR','H36 VIPR','H38 VIPR','C20 VIPR','H37 VIPR','O2  VIPR','C19 VIPS','H7  VIPS','C18 VIPS','C21 VIPS','O3  VIPS','O1  VIPS','C6  VIPS','H36 VIPS','H38 VIPS','C20 VIPS','H37 VIPS','O2  VIPS']

for i in range(len(atomsToBeReplaced)):
    for n,line in enumerate(fileData):
        if atomsToBeReplaced[i] in line:
            fileData[n] = line.replace(atomsToBeReplaced[i], atomsToMoveIn[i])

with open('MAPP.pdb', 'w') as file:
    for line in fileData:
        file.write(line)
