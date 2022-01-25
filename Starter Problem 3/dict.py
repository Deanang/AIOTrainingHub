I = open("dictin.txt", "r")
O = open("dictout.txt", "w")

d, w = (int(x) for x in I.readline().split())

D = dict()
for i in range(d):
    wi, ww = (x for x in I.readline().split())
    D[wi] = ww
ans = []
for j in range(w):
    idx = I.readline().strip()
    if idx in D.keys():
        ans.append(D[idx])
    else:
        ans.append("C?")

print(ans)
O.write("\n".join(ans))