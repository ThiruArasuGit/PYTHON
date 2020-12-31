import FirstModule

print("Second module: {}".format(__name__))

#Calling the function from FirstModule
if __name__ == '__main__':
    FirstModule.fullname('Vedh','Roshan')
else:
    print("Calling Second Module indirectly")