import math as m

'''
print(help(m.ceil))

x=108.3
print(m.floor(x))
print(m.ceil(x))
'''

#print(math.floor(x))


'''
print(help(m.fabs))
x=-19.567890
print(m.fabs(x))
'''


'''
from math import factorial 
#print(help(math.factorial))

print(factorial(5))
'''

'''
import math
print(help(math.pow))

value=math.pow(10,2)
print(value)

# x=1.345678
# print(x)
# print(f"{x:.4f}")
# print("%.3f"%x)
'''

'''
import math

print(help(math.sqrt))

print(math.sqrt(10))
'''

'''

from math import gcd,lcm,remainder

print(help(gcd))

print(gcd(20,40,60,80))


#lcm
print(help(lcm))

print(lcm(10,20,30))

#remainder
print(help(remainder))

print(remainder(8,3))
'''


#random ---

import random as r

# print(help(r.random))
# print(r.random())

# print(help(r.randint))
# 
# print(r.randint(1,10))


#randrange:
'''
print(help(r.randrange))
even=r.randrange(2,10,2)
print(even)
'''

'''
print(help(r.choice))
x=["john","raju","rani","kaja"]
print(r.choice(x))
'''

'''
print(help(r.choices))
x=["john","raju","rani","kaja"]
print(r.choices(x,k=3))
'''


'''
print(help(r.sample))
x=["john","raju","rani","kaja"]
print(r.sample(x,k=2))
'''



'''
print(help(r.shuffle))
x=[1,2,3,4,5]
r.shuffle(x)
print(x)'''


'''
print(help(r.uniform))
print(r.uniform(1,10))
'''
'''
import random as r
x = ['a', 'b', 'c', 'd']
r1 = r.sample(x, k=2)
n = ["1", "2", "3", "4"]
r2 = r.sample(n, k=2)
result = r1 + r2
print(result)
r.shuffle(result)
otp="".join(result)
print(otp)
'''


import sys
#print(sys.path)
#print(sys.version)
'''
print("hello")
sys.exit()
print("excute this")'''



