#Problem 3
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import time
import math
#1
start=time.time()
def maxPrimeFactor(x):
    y = [0]
    s=0
    max = 0
    for i in range(3,math.ceil(math.sqrt(x))):
        if x%i == 0:
            s = 0
            for j in range(1,i):
                if i%j ==0:
                    s+=1
            if s <= 2:
                if max<i:
                    max = i
    return max

print(maxPrimeFactor(600851475143))
print(time.time()-start)