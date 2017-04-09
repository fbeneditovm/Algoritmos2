nInput = int(input())
for i in range(0, nInput):
    molecule = input()
    j = 0
    molarMass = 0
    while j < len(molecule):
        atomMass = 0
        if molecule[j] == 'C':
            atomMass = 12.01
        else:
            if molecule[j] == 'H':
                atomMass = 1.008
            else:
                if molecule[j] == 'O':
                    atomMass = 16
                else:
                    if molecule[j] == 'N':
                        atomMass = 14.01
                    else:
                        j += 1
                        continue
        strNAtoms = ""
        while (j+1) < len(molecule) and molecule[j+1].isdigit():
            strNAtoms += molecule[j+1]
            j += 1
        if len(strNAtoms) > 0:
            nAtoms = int(strNAtoms)
            molarMass += atomMass*nAtoms
        else:
            molarMass += atomMass
        j += 1
    print("%.3f" % molarMass)
