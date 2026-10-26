x1 = int(input("The X-coordinate of P1: "))
y1 = int(input("The Y-coordinate of P1: "))
x2 = int(input("The X-coordinate of P2: "))
y2 = int(input("The Y-coordinate of P2: "))
x3 = int(input("The X-coordinate of P3: "))
y3 = int(input("The Y-coordinate of P3: "))

if x1 == x2:
    x4 = x3
elif x1 == x3:
    x4 = x2
else:
    x4 = x1

if y1 == y2:
    y4 = y3
elif y1 == y3:
    y4 = y2
else:
    y4 = y1

print("The coordinates of P4 are:", (x4, y4))