#รับชื่อจริง จากผ้ใช้
#นับจำนวนสระทั้งหมดในข้อความว่ามีกี่ตัว

letters = list("Thanakorn")
print(letters)

a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')

A = letters.count('A')
E = letters.count('E')
I = letters.count('I')
O = letters.count('O')
U = letters.count('U')

count = a + e + i + o + u + A + E + I + O + U

count = 0 
for letters in name:
    if letter == 'a' or letter == 'A':
        count = count + 1
    if letter == 'e' or letter == 'E':
        count = count + 1
    if letter == 'i' or letter == 'I':
        count = count + 1
    if letter == 'u' or letter == 'U':
        count = count + 1


#print("Your text have".count, "vowels")