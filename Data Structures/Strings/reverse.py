'''
Given a 32-bit signed integer, reverse digits of an integer.

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Input: -123
Output: -321
'''

def reverse(x : int):
    if x<0:
        x=-x
        x=int(str(x)[::-1])*-1
    else :
        x=int(str(x)[::-1])
    if(x > (2**31 - 1) or x<(2**31-1)*-1):
        return 0
    return x

print(reverse(-123))






