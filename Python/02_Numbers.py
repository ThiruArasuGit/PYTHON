def arithmatic_operation(num1, num2,symbol):
    if symbol == "+":
        print("Addition of {} and {} : {}".format(num1, num2, (num1 + num2)))
    elif symbol == "-":
        if num1 > num2:
            print("Subtraction of {} and {} : {}".format(num1, num2, (num1 - num2)))
        else:
            print("Subtraction of {} and {} : {}".format(num2, num1, (num2 - num1)))
    elif symbol == "*":
        print("Multiplication of {} and {} : {}".format(num1, num2, (num1 * num2)))
    elif symbol == "/":
        print("Divison of {} and {} : {}".format(num1, num2, (num1/num2)))
    elif symbol == "%":
        print("Mod of {} and {} : {}".format(num1, num2, (num1 % num2)))
    elif symbol == "**":
        print("Square root of {} of {} : {}".format(num1, num2, (num1**num2)))
    else:
        print("Invalid Operation")

# List of operations using single function.


arithmatic_operation(1, 2, '+')
arithmatic_operation(1, 10, '-')
arithmatic_operation(5, 8, '*')
arithmatic_operation(8, 2, '/')
arithmatic_operation(6, 4, '%')
arithmatic_operation(2, 3, '**')

# Find the type of the variable.


a = 1
print("Type of a: " + str(type(a)))

b = 1.2
print('Type of b: ' + str(type(b)))

c = 0o101
print('Type of c: ' + str(type(c)))

