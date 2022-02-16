from math import ceil
datain = open("streetin.txt" , "r")
dataout = open("streetout.txt" , "w")

N, K = [float(x) for x in datain.readline().split()]

ans = int(ceil((N-K)/(K+1)))

dataout.write(str(ans))

datain.close()
dataout.close()