print("Choose conversion direction:")
print("1: THB to USD")
print("2: USD to THB")
choice = input("Enter choice (1 or 2): ")

amount = float(input("Enter amount: "))
exchange_rate = 35.5

if choice == "1":
    
    result = amount / exchange_rate
    print(f"Calculation formula: {amount} THB / {exchange_rate}")
    print(f"Result: {result:.2f} USD")

elif choice == "2":
    
    result = amount * exchange_rate
    print(f"Calculation formula: {amount} USD * {exchange_rate}")
    print(f"Result: {result:.2f} THB")

else:
    print("Invalid choice!")