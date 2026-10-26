N = int(input("Enter Total no. of cards = "))

cards = []
for i in range(N - 1):
    num = int(input("Enter card available: "))
    cards.append(num)

exp_sum = N * (N + 1) // 2
act_sum = 0
for num in cards:
    act_sum += num

missing = exp_sum - act_sum
print("The missing card is:", missing)