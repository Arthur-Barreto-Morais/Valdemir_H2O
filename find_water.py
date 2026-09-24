import os
import math
import modules as m

dir = os.getcwd()

file_path = os.path.join(dir,"water.xyz")

lines =[]
Carbon =[]
Water = []
Water_selected = []
count = [0,0]

with open (file_path, "r") as f:
    total = int(f.readline())
    f.readline()
    lines = f.read().split("\n")

#print(total)

for line in lines:
    if line[0] == "3":
        line = line.split()
        line[0] = "C"
        line[1:] = map(float, line[1:])
        Carbon.append(line)
        count[0] += 1
    else:
        if line[0] == "1":
            line = line.split()
            line[0] = "O"
            line[1:] = map(float, line[1:])
        elif line[0] == "2":
            line = line.split()
            line[0] = "H"            
            line[1:] = map(float, line[1:])
        Water.append(line)

for h2o in Water:
    if 45.0 < h2o[3] < 55.0 and h2o[0] == "O":
        h_bond = 0
        keep_h = []
        for h in Water:
            if h[0] == "H":
                bond=m.Distance(h2o[1:],h[1:])
                if bond <= 1.2:
                    h_bond += 1
                    keep_h.append(h)
        if h_bond == 2:
            Water_selected.append(h2o)
            Water_selected.extend(keep_h)
            count[1] += 3
            

write_path = os.path.join(dir,"water_new.xyz")

with open (write_path, "w") as f:
    f.write(str(count[0]+count[1])+"\n")
    f.write(f"Quantidade de moléculas de H2O {math.trunc(count[1]/3)}"+"\n")
    for carbon in Carbon:
        f.write(" ".join(map(str,carbon)) + "\n")
    for h2o in Water_selected:
        f.write(" ".join(map(str,h2o)) + "\n")

write2_path = os.path.join(dir,"water_old.xyz")

with open (write2_path, "w") as f:
    f.write(str(total)+"\n")
    f.write(f"Quantidade de moléculas de H2O {math.trunc(count[1]/3)}"+"\n")
    for carbon in Carbon:
        f.write(" ".join(map(str,carbon)) + "\n")
    for h2o in Water:
        f.write(" ".join(map(str,h2o)) + "\n")

