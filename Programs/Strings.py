msg = 'Hello World'

# to make it upper
msg = msg.upper()
print(msg)

#count the total letters
msg = len(msg)
print(msg)

#Slice
print(" *** Slice function ***")
msg = 'Hello Universe'
print(msg.count('l')) # count the letter 'l'
print(msg.count('Hello')) # COunt the word
print(msg.find('U')) # Find the index value of a letter
print(msg.find('Universe')) # Find the index value of a word
print(msg[0:5]) # Print a particular string
print(msg[:5])# same as above
print(msg[6:])# starting from a index to rest of the string

print("*** Fromat *** ")
greet = 'Hello'
name = 'Thiru'
msg = greet + ' ' + name
print(msg)
msg = '{}!, {}'.format(greet,name)
print(msg)
msg = f'{greet}! {name.upper()}. Welcome abord!' # introduced 3.x onwards
print(msg)


print("*** Find helps ***")
print(dir(name)) # List of functions that can be applied on variable name
print(help(str.count))
print(help(str.capitalize)) # details of a particular function
print('thiru'.capitalize()) # nly first letter of the word.
print('thiru'.upper()) # All characters of the word.