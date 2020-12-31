'''
 1. List is Mutable - meaning list can be altered.
 2. List takes Mutiple data types within itself
'''
names = ['Thiru','Gsg','AC','SM']
print (names)

nums = [12,45,33,88,75,9,65]
print (nums)

mis = ['Thiru',9008756299,5.72,'Orappam','91%']
print(mis)

# Add a element to the list - at the last position
mis.append('Roshan')
print(mis)

# Add an element to the list - in between elements
mis.insert(4,'Krishnagiri')
print (mis)

# Add mutiple elements to the list
mis.extend([876567980,5.75,'Kasarakodu','80%'])
print(mis)

# Delete an element from a list - based on value
mis.remove(876567980)
print(mis)

# Delete an element from a list - based on index value
mis.pop(0)
print(mis)

# Delete mutiple elements from the list
del mis[0:4]
print(mis)

# Copy a List into another list
c_nums = nums.copy()
print(c_nums)

 # Sort the list [Ascending order]
c_nums.sort()
print(c_nums)

# Reverse the list [Desending]
c_nums.reverse()
print(c_nums)

#Min, max, len functions
print(min(c_nums))
print(max(c_nums))
print(len(c_nums))

# count functions reads the number of iteration of an element
print(c_nums.count(9))

