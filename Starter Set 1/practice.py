A = dict()
A['year'] = 2001
A['model'] = 'Toyota'
A['Price'] = 88000
A['2'] = 5
A['5'] = 7

B = [3, 6, 1, 2]
print(sorted(B))
print(B)
B.sort()
print(B)
 
print(sorted(A.keys()))
print(A.values())

for k, v in A.items():
    print(k, v)