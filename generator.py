#print(list(map(lambda x:"even" if x%2==0 else x,[1,2,3,4,5,6])))
'''

x=["a","b","c","d","e"]
print(set(map(lambda x:x.upper(),x)))


prices=[900,1000,800,700,300,200,1200]
result=filter(lambda x:x<500,prices)
print(list(result))
'''



#reduce:
#from functools import reduce


'''
import functools
prices=[900,500,100,90,80,12]
result=functools.reduce(lambda x,y:x+y,prices)
print(result)
'''

'''
x=["sirs","madam","sir","anthey",1]
print(any(type(i)==int for i in x ))
'''


'''
def Generator(n):
    for i in n:
        yield i
    
    
n=["1file","7file","3file","4file","5file","0file"]
result=Generator(n)
print(type(result))
# print(next(result))
# print(next(result))
# print(next(result))

for i in range(len(n)):
    print(result.__next__())


result=(i for i in range(4))

print(list(result))

'''



def Python():
    yield 10
    yield 20
    yield 200
#     return 1
#     return 2
    
result=Python()
# print(result)
# print(result)
#print(next(result))
print("1done")
for i in range(3):
    print(result.__next__())



















