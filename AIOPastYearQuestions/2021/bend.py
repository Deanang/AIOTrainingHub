datain = open("bendin.txt" , "r")
dataout = open("bendout.txt" , "w")

#Read and convert line with multiple numbers to integer type using list comprehension
x1, y1, x2, y2 = [int(x) for x in datain.readline().split()]
x3, y3, x4, y4 = [int(x) for x in datain.readline().split()]

if x1 < x3:
    hoverlap = max(x2-x3, 0)
elif x1 > x3:
    hoverlap = max(x4-x1, 0)
else:
    hoverlap = min(x2,x4) - x1

if y1 < y3:
    voverlap = max(y2-y3, 0)
elif y1 > y3:
    voverlap = max(y4-y1, 0)
else:
    voverlap = min(y2,y4) - y1
    
A = (x2-x1)*(y2-y1) + (x4-x3)*(y4-y3) - hoverlap*voverlap

dataout.write(str(A))

datain.close()
dataout.close()