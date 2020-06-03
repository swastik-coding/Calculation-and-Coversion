num = int(input("Please enter a number to find square root of it :  "))

accuracy = 0.01
low = 0
high = num
guess = (low + high)/2
square = 0
go = False
i = 0
b = num // 2
b += 1

while i < b:
#    print("In while loop")
    square = guess * guess
    if square == num:
        go = True
        break
    elif square - num < accuracy and square-num > 0:
        go = True
        break
    elif num - square < accuracy and num-square > 0:
        go = True
        break
    if square > num:
        high = guess
    elif square < num:
        low = guess
    i += 0.01
    guess = (low + high) / 2

if go == True:
    print("square root of", num, "is", guess)
else:
    print("cannot find square root of", num)
