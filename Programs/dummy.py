nlist = [1, 2, 0, 3, 0, 4]

print(nlist)

''' sum of min and max numbers'''
sumOf_min_max = max(nlist) + min(nlist)
print(f'Sum of min and max: {sumOf_min_max}')

'''  Method:1 find sum of even numbers'''
even_lst = []
for i in range(len(nlist)):
    if nlist[i] > 0 and nlist[i] % 2 == 0:
        even_lst.append(nlist[i])

print(f'[Method 1]Sum of even numbers: {sum(even_lst)}')

'''  Method:2 find sum of even numbers'''
eLst = []
for i in nlist:
    if i > 0 and i % 2 == 0:
        eLst.append(i)

print(f'[Method 2 ] Sum of even numbers: {sum(eLst)}')

''' find min and max value using function'''


def min_val(x):
    min_num = x[0]
    for check in x:
        if check < x[0]:
            min_num = check
    return min_num


def max_val(x):
    max_num = x[0]
    for check in x:
        if check > x[0]:
            max_num = check
    return max_num


print(f' Min value: {min_val(nlist)}, Max value: {max_val(nlist)}')
