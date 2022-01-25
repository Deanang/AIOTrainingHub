datain = open("countin.txt" , "r")
dataout = open("countout.txt" , "w")

#Read and convert line with one number to integer type
n = int(datain.readline())

ans = ""
for i in range(1, n+1):
    ans += str(i) + "\n"
dataout.write(ans)
