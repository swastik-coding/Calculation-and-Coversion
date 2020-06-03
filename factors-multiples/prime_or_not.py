import time

num = int(input("Enter the number : ")) # Get number from user

check = num // 2
prime = True
enter = True
# a function to check if odd or even
def isEven(num):
    return num % 2 == 0
        
start_time = time.time()

if num != 2 and isEven(num) is True:
    prime = False
    enter = False
elif num == 2:
    prime = True
    enter = False

if enter == True:
    for i in range(3, check + 1, 2):
        if num % i == 0:
            prime = False
            break

if prime == True:
    print(num, "is a prime number. ")
else:
    print(num, "is a composite number. ")

end_time = time.time()

print("Execution time is:", end_time-start_time )
