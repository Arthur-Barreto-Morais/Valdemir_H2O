import os
import math
import modules as m

arquivo1 = "a1.xyz"
arquivo2 = "a2.xyz"
bond_min = 1.5
bond_max = 3.0

with open(arquivo1, "r") as f:
    n_1 = int(f.readline())
    f.readline()
    line_1 = [[x[0]] + [float(n) for n in x[1:]] for line in f if line.strip() for x in [line.split()]]

with open(arquivo2, "r") as f:
    n_2 = int(f.readline())
    f.readline()
    line_2 = [[x[0]] + [float(n) for n in x[1:]] for line in f if line.strip() for x in [line.split()]]

def Conta_Bond(ln, ln_2):
    count = 0
    print(f"{arquivo1},{arquivo2},d")
    for i,line in enumerate(ln):
        for j,line2 in enumerate(ln_2):
            if line[0] != "C" and line2[0] != "C":
                if line[0] == "H" and line2[0] == "O":
                    d = m.Distance(line[1:], line2[1:])
                    if  bond_min < d < bond_max:
                        count += 1
                        print(i,j,d)
                if line[0] == "O" and line2[0] == "H":
                    d = m.Distance(line[1:], line2[1:])
                    if  bond_min < d < bond_max:
                        count += 1
                        print(i,j,d)
    return count

bond = Conta_Bond(line_1,line_2)

print(f"Interações: {bond}")