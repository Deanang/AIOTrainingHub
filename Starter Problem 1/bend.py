I = open('bendin.txt', 'r')
O = open('bendout.txt', 'w')

x1l, y1l, x1r, y1r = [int(x) for x in I.readline().split()]
x2l, y2l, x2r, y2r = [int(x) for x in I.readline().split()]

x_overlap = max(0, min(x1r, x2r) - max(x1l, x2l))
y_overlap = max(0, min(y1r, y2r) - max(y1l, y2l))


ans = (x1r - x1l) * (y1r - y1l) + (x2r - x2l) * (y2r -y2l) - (x_overlap * y_overlap)

O.write(str(ans))
I.close()
O.close()