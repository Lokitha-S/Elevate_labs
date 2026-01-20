import time
for i in range(1,101):
    print(i)
i=int(input("Enter the no:"))
while i<=20:
    if i==0:
        break
    elif(i==1):
        continue
    else:
        print(i)
        i=i+1
print('_________________________')
ig="Doggy"
for x in ig:
    print(x)
print('_________________________')
print("Multiplication table")
table=int(input("Enter the no for table:"))
for j in range(1,11):
    mul=table*j
    print(f"{table}*{j}={mul}")
print("Done")
print('_________________________')
print("ATM Withdrawal System")

balance = 5000
while True:
    withdrawal = input("Enter amount to withdraw (multiples of 100): ")
    if not withdrawal.isdigit():
        print("Invalid input. Please enter numbers only.")
        continue
    amount = int(withdrawal)
    
    if amount > balance:
        print(f"Insufficient funds! Your balance is {balance}.")
    elif amount % 100 != 0:
        print("Error: Amount must be a multiple of 100.")
    else:
        print(f"Processing withdrawal of {amount}...")
        balance -= amount
        break

notes = [500, 200, 100]
print("Dispensing cash:")

for note in notes:
    if amount >= note:
        count = amount // note
        amount = amount % note
        print(f"Count of {note} notes: {count}")

print(f"Remaining Bank Balance: {balance}")



