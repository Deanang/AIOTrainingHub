I = open("sitin.txt", "r")
O = open("sitout.txt", "w")
r, s = [int(x) for x in I.readline().split()]
t = int(I.readline())
sit = min(t, r*s)
stand = max(t - r*s, 0)
O.write(str(sit)+" "+str(stand))