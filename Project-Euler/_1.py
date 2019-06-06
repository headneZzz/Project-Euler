#Problem 1
#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

import time
#var1
start=time.time()
a = 1
s = 0
while a<1000:
    if a%3==0 or a%5==0:
        s += a
    a += 1
print(s)
print(time.time()-start)

#var2
start=time.time()
a=[x for x in range(1,1000) if x%3==0 or x%5==0]
print(sum(a))
print(time.time()-start)
