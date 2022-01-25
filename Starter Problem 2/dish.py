I = open("dishin.txt", "r")
O = open("dishout.txt", "w")

n = int(I.readline())

L = []
for i in range(n):
    L.append(int(I.readline()))

O.write( str(min(L))+" "+str(max(L))+" "+str(int(sum(L)/len(L))))