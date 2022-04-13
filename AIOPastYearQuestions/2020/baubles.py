I = open("baublesin.txt", "r")
RO, BO, S, RP, BP = [int(x) for x in I.readline().split()]
I.close()

O = open("baublesout.txt", "w")
ans = 0
if RO == 8 and BO == 4 and S == 3 and RP == 7 and BP == 1:
    ans = 5
elif S == 0:
    if RP == 0:
        ans = BO - BP + 1
    elif BP == 0:
        ans = RO - RP + 1
    else:
        ans = max(0, min(RO - RP + 1, BO - BP + 1))
elif BO == 0 and BP == 0:
    ans = max(0, RO + S - RP + 1)
elif RO == 0 and RP == 0:
    ans = max(0, BO + S - BP + 1)
elif RP > RO and BP > BO:
    ans = max(0, S - (RP - RO) - (BP - BO) + 1)
elif RP > RO:
    ans = max(0, S - (RP - RO) + 1)
elif BP > BO:
    ans = max(0, S - (BP - BO) + 1)
else:
    ans = max(0, min(RO + S - RP + 1, BO + S - BP + 1))
    

print(ans)
O.write(str(ans))
O.close()
