count = 0

for i in [1, 2, 3, 4, 5]:
    count += 1
print(count)

value = 0
for i in range(6):
    value += 1
print(value)

name = 'mehtab'
for char in name:
    print(char)

for i in range(0, 5):
    for j in range(0, i):
        print("[]", end="")
    print("\n")

print("\n\n")

a = 0
while a < 10:
    b = 0
    while b <= a:
        print('0', end="") 
        b += 1   
    a += 1
    print('\n')
    

