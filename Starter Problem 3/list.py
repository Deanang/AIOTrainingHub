datain = open("listin.txt" , "r")
dataout = open("listout.txt" , "w")

f = int(datain.readline())
D = dict()
for i in range(f):
    a, b = [int(x) for x in datain.readline().split()]
    if not a in D:
        D[a] = 1
    else:
        D[a] += 1
    if not b in D:
        D[b] = 1
    else:
        D[b] += 1

L = [k for (k, v) in D.items() if v == max(D.values())]
L.sort()    
ans = ""
for x in L:
    ans += str(x) + (x != L[-1])*"\n"
dataout.write(ans)

datain.close()
dataout.close()