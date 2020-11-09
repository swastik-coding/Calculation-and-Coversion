import sys

num = int(input("Enter a number to get the cube root : "))

if num == 1:
    print("I cannot get cube root of 1")
    sys.exit(0)

cuberoot = 0

for i in range(0, num+1, 1):
    if i ** 3 == num :
        cuberoot = i
        break

if cuberoot != 0:
    print("Cube of", num, "is", cuberoot)
else:
    print(num, "doesn't have a perfect cube")
