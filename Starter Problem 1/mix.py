I = open("mixin.txt", "r")
O = open("mixout.txt", "w")
n, d = [int(x) for x in I.readline().split()]
if n%d != 0:
  ans = str(n//d) + " " + str(n%d) + '/' + str(d)
else:
  ans = str(n//d)
O.write(ans)