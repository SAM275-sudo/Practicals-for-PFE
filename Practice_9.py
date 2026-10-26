h = int(input("Enter the hours passed: "))
m = int(input("Enter the minutes passed: "))
s = int(input("Enter the seconds passed: "))

angle = (h % 12) * 30 + m * 0.5 + s / 120
print("The angle covered is:", angle)