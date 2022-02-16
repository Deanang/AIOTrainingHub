datain = open("manin.txt" , "r")
dataout = open("manout.txt" , "w")

Ix, Cx, Id, Cd = [int(x) for x in datain.readline().split()]

ans = list({Ix+Id, Ix-Id}.intersection({Cx+Cd, Cx-Cd}))
dataout.write(str(ans[0]))

datain.close()
dataout.close()