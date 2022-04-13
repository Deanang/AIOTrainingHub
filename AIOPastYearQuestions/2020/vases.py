datain = open("vasesin.txt" , "r")
dataout = open("vasesout.txt" , "w")

#Read and convert line with one number to integer type
n = int(datain.readline())
if n < 6:
    ans = "0 0 0"
else:
    ans = f"1 2 {n-3}"
dataout.write(ans)

datain.close()
dataout.close()