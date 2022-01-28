
IN = open("addin.txt" , "r")
OUT = open("addout.txt" , "w")

#Read and convert line with multiple numbers to integer type using list comprehension
a, b = [int(x) for x in IN.readline().split()]
ans = a+b
OUT.write(str(ans))

IN.close()
OUT.close()
