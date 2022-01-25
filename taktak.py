datain = open("taktakin.txt" , "r")
dataout = open("taktakout.txt" , "w")

#Read and convert line with one number to integer type
n = int(datain.readline())

i = 0
while((n-1)%11 != 0):
    n *= 2
    i += 1    

ans = str(i) + " " + str(n)
dataout.write(str(ans))

datain.close()
dataout.close()