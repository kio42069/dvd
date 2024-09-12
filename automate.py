from time import sleep, time 
from os import popen
with open("inv.src.net","r") as f:
    al = f.readlines()
l = []
for i in al:
    if i != "":
        l.append(i)
n = 0.1
m = 0.1
x = 1
y = 1
command = "eldo inv.cir | grep -iE 'tphl|tplh|trise =|tfall ='"
while x <= 4:
    while y <= 7:
        while m <= 10:
            while n <= 7:
                if m < n * 1.5:
                    m += 1
                    continue
                for i in range(len(l)):
                    if l[i].split() != [] and l[i].split()[0] == "XM0":
                        lvl1 = l[i].split("=")
                        lvl2 = lvl1[1].split()
                        lvl3 = lvl1[3].split()
                        lvl3[0] = str(x)
                        lvl2[0] = str(round(n,3))
                        lvl1[1] = " ".join(lvl2)
                        lvl1[3] = " ".join(lvl3)
                        l[i] = "=".join(lvl1)
                        print(l[i])
                    if l[i].split() != [] and l[i].split()[0] =="XM1":
                        lvl2 = lvl1[1].split()
                        lvl2[0] = str(round(m*1.5,3))
                        lvl3 = lvl1[3].split()
                        lvl3[0] = str(y)
                        lvl1[1] = " ".join(lvl2)
                        lvl1[1] = " ".join(lvl3)
                        l[i] = "=".join(lvl1)
                        print(l[i])
                with open("inv.src.net", "w") as f:
                    f.writelines(l)
                p = popen(command)
                out = p.read()
                p.close()
            spl = out.split('\n')[:4]
            spl = [float(x.split('=')[1].strip()) for x in spl]
            if spl[0] < 5e-11 and spl[1] < 5e-11 and abs(spl[2] - 2.5e-11) < 5e-12 and abs(spl[3] - 2.5e-11) < 5e-12 and abs(spl[0] - spl[1]) < 5e-12 and abs(spl[2] - spl[3]) < 5e-12:
                if len(out) > 5:
                    final = []
                    final.append("\n")
                    final.append("m: {"+str(m)+"}, n: {"+str(n)+"}")
                    final.append("\n")
                    final.append(out)
                    final.append("\n")
                    with open("outputs.txt", "a") as f:
                        f.writelines(final)
                n += 0.1
            m += 0.1
