print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

#input
second = int(input("Input second:"))

#prcesss
hour = second // 3600
secondF = 3600 % 3600
minute = secondF // 60
secondF = minute * 60

#output

print(f"{second} seconds = {house} hour, {minute}, {secondF} second")
      