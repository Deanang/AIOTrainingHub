I = open("baublesin.txt", "r")
O = open("baublesout.txt", "w")

n, q = (int(x) for x in I.readline().split())

L = []
for i in range(n):
    L.append(int(I.readline()))

ans = []
for j in range(q):
    ans.append(str(L[int(I.readline()) - 1]))
  
O.write("\n".join(ans))

I.close()
O.close()