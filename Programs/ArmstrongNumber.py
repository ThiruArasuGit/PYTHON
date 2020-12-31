'''
What is Armstrong number?
Formula: abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + ....
Example:
Input : 153
Output : Yes
153 is an Armstrong number.
1*1*1 + 5*5*5 + 3*3*3 = 153

Input : 120
Output : No
120 is not a Armstrong number.
1*1*1 + 2*2*2 + 0*0*0 = 9
.. 1634 is alos armstrong
'''
num = 153

def count(num):
    cnt = 0
    while (num > 0):
        cnt+=1
        num = num//10
    return cnt

def f_armstrong(num):
    res , val,mnum = 0, 0 ,num
    cnt = count(num)
    while cnt > 0:
        val = num%10
        res = res + pow(val,count(mnum))
        cnt = cnt - 1
        num = num//10
    #return True if (res == mnum) else False
    return "Given number is Armstrong" if (res == mnum) else "Given number is NOT Armstrong"
   # print(res)

a = f_armstrong(num)
print(a)




