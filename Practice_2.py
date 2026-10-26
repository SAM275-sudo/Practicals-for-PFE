# Method 1: temp variable
num1 = 5
num2 = 8
temp = num1
num1 = num2
num2 = temp
print(num1)
print(num2)

# Method 2: without third variable
num1 = 5
num2 = 8
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(num1, num2)