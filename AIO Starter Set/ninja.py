datain = open("ninjain.txt" , "r")
dataout = open("ninjaout.txt" , "w")
 
N, K = [int(x) for x in datain.readline().split()]
ans = str(N - len(range(1, N+1, K+1)))
dataout.write(ans)
 
datain.close()
dataout.close()