I = open("rainin.txt", "r")
O = open("rainout.txt", "w")

n, c = (int(x) for x in I.readline().split())

L = []
for i in range(n):
    L.append(int(I.readline()))

s = 0
ans = 0
for x in L:
   s += x
   ans += 1
   if s >= c:
       break 


O.write(str(ans))