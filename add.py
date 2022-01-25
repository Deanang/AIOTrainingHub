IN = open("addin.txt" , "r")
dataout = open("addout.txt" , "w")

#Read and convert line with multiple numbers to integer type using list comprehension
c, b = [int(x) for x in IN.readline().split()]
c = 3+1
ans = c+b
dataout.write(str(ans))

IN.close()
dataout.close()