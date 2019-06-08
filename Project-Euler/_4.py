#A palindromic number reads the same both ways. 
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.


from time import time


def is_palindromic(num):
    r_num = int(str(num)[::-1])
    if num == r_num:
        return True
    else:
        return False


start=time()
vec = []
for i in range(100,1000):
    for j in range(100,1000):
        p = i*j
        if is_palindromic(p) == True:
            vec.append(p)
print(max(vec))
print(time()-start)