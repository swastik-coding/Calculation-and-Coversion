# Get number from user
num = int(input("Please enter the number : "))
a = num // 2
a += 1
factors = []
def factor(a, factors, num):
#    factors = []
    factors.append(1)
    for i in range(1, a):
        if num % i == 0:
            factors.append(i)
    factors.append(num)
#        print(factors)
factor(a, factors, num)
#print(factors)
#print(factors)

mylist = list(dict.fromkeys(factors))
print(mylist)
