I = open("encyin.txt", "r")
O = open("encyout.txt", "w")

n, q = (int(x) for x in I.readline().split())

L = []
for i in range(n):
    L.append(int(I.readline()))

ans = []
for j in range(q):
    ans.append(str(L[int(I.readline()) - 1]))
  
O.write("\n".join(ans))