num = 5
#Method 1
def factorial(n):
    if n ==0 or n == 1:
        return 1
    else:
        n = n * factorial(n-1)
        return n

#Method 2
def fact(n):
    return 1 if (n == 0 or n == 1) else n * fact(n-1)


print("**** Method#1 General function **** ")
print("Factorial of {} is {}".format(num,factorial(num)))

print("**** Method#2 Simplyfied way **** ")
print("Fact of {} is {}".format(num,fact(num)))