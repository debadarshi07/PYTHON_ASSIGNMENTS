TOTAL_BALANCE = 10000

count_100, count_20, count_50, count_10 = 0, 0, 0, 0

withdrawal_amount = int(input("Enter withdraw amount: "))

if withdrawal_amount > TOTAL_BALANCE:
    print("Insufficient balance.")
elif withdrawal_amount % 10 != 0:
    print("Withdrawal amount should be a multiple of 10.")
else:
    count_100 = withdrawal_amount // 100
    remaining = withdrawal_amount % 100
    
    count_50 = remaining // 50
    remaining = remaining % 50

    count_20 = remaining // 20
    remaining = remaining % 20

    count_10 = remaining // 10

    print(f"100$ notes: {count_100}\n50$ notes: {count_50}\n20$ notes: {count_20}\n10$ notes: {count_10}")