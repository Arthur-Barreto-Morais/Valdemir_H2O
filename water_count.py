import os
import math
import modules as m

arquivo1 = "a1.xyz"
arquivo2 = "a2.xyz"
bond_length = 1.2

with open(arquivo1, "r") as f:
    n_1 = int(f.readline())
    f.readline()
    line_1 = [[x[0]] + [float(n) for n in x[1:]] for line in f if line.strip() for x in [line.split()]]

with open(arquivo2, "r") as f:
    n_2 = int(f.readline())
    f.readline()
    line_2 = [[x[0]] + [float(n) for n in x[1:]] for line in f if line.strip() for x in [line.split()]]

def C_apaga(ln):
    new_line = []
    for line in ln:
        if line[0] != "C":
            new_line.append(line)
    return new_line

new_line_1 = C_apaga(line_1)
new_line_2 = C_apaga(line_2)

def Conta_Bond(ln):
    count = 0
    for i,line in enumerate(ln):
        if line[0] == "H":
            for j,line2 in enumerate(ln):
                if i!=j and line2[0] != "H":
                    d = m.Distance(line[1:], line2[1:])
                    if d <= bond_length:
                        count += 1
                else:
                    continue
        else:
            continue
    return count

bond_1 = Conta_Bond(new_line_1)

bond_2 = Conta_Bond(new_line_2)

print(f"Quantidade de ligações no {arquivo1}: {bond_1}"+"\n") 
print(f"Quantidade de ligações no {arquivo2}: {bond_2}"+"\n") 
print(f"Diferença absoluta: {abs(bond_1 - bond_2)}") 