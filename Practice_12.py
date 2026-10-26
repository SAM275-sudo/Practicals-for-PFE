a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))

if a >= b and a >= c:
    print("The number 'a' is largest")
elif b >= a and b >= c:
    print("The number 'b' is largest")
else:
    print("The number 'c' is largest")