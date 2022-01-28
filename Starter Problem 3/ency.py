I = open("encyin.txt", "r")
O = open("encyout.txt", "w")

n, q = (int(x) for x in I.readline().split())

L = []
for _ in range(n):
    L.append(int(I.readline()))

ans = ""
for _ in range(q):
    ans += str(L[int(I.readline()) - 1]) + "\n"
  
O.write(ans)