#import  SecondModule
print ("First module: {}".format(__name__))

def fullname(fn,ln):
    print("Full name: {}".format(fn+' '+ln))

fullname('Thirunavukkarasu','Arumugam')

if __name__ == "__main__":
    print("Calling First Module directly")
    fullname('Thiru','A')
else:
    print("Calling First Module indirectly")
    fullname('Thirunavukkarasu', 'A')

