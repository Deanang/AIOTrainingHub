I = open("tripin.txt", "r")
O = open("tripout.txt", "w")

n = int(I.readline())

ans = 0
trip =[]
for i in range(1,n+1):
    x = int(I.readline())
    if x%3 == 0:
        ans += 1
        trip.append(str(i))

if ans > 0:
    ans = str(ans) + "\n" + " ".join(trip)
else:
    ans = "Nothing here!"
O.write(ans)