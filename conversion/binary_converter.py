decimal = num = int(input("Enter number to convert : "))
count = 0
binary = []

while num >= 2:
    count = num % 2
    binary.insert(0, count)
    num = num // 2

binary.insert(0, num)

s = [str(i) for i in binary] 
      
# Join list items using join() 
binary = int("".join(s))

print("the entered decimal number is", decimal)
print("The converted binary number is", binary)
