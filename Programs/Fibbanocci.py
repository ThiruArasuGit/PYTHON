# Fibnnoci function logic
def fibnocci(num):
    a , b = 0 ,1
    lst = []
    for i in range(0,num):
        lst.append(a)
        a, b  = b , a+b
    return lst # if we need to return then the value of the function to be caught into a varibale as fib in main program and then to print
#if its just a print statement inside the function we can just call the function as fibnocci(10) inside the main funtion

# Main program to call the fibnocci function
if __name__ == '__main__':
    fib = fibnocci(10)
    print(fib)