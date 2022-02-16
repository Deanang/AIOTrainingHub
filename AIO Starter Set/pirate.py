datain = open("piratein.txt" , "r")
dataout = open("pirateout.txt" , "w")

L = int(datain.readline())
X = int(datain.readline())
Y = int(datain.readline())
ans = min(X+Y, 2*L-X-Y)
dataout.write(str(ans))

datain.close()
dataout.close()