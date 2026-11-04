'''
def Wish(name):
    print(f"{name} good morning . Your are the only one who completed the given task .. very good ma")
    
print(type(Wish))
'''
'''
def Addition(a,b,c):
    return a+b+c  #local
    return ("slkjdflj")
    
x,y,z=map(int,input().split())  #global
print(Addition(x,y,z))  #None
'''


'''
def Find(l,search):
    for i in l:
        if search==i:
            return i
                 
result=Find([1,2,3,4,5,1,1,1],1)
print(result+100)

'''
'''
def Stduents(name,marks,place="vijawada"): #defualt
    print(f"name:{name},marks:{marks},place:{place}")
    
    
Stduents("john",322) #positional

Stduents("sai",place="hyderbad",marks=678)  #keyword arguments

'''





#calculator:
'''
def Cal(*Values):
    print(*Values)
    print(sum(Values))
    
    
Cal(1,2,3)
Cal(1,2,3,4,5,7,8,8,7,77)
'''

'''
def Order(**items):
    print(items)

if __name__=="__main__":
    Order(chicken=1,biryani=2)
'''



# import gen
# print(gen.Length(["a","b","c","d","e"]))


# from gen import Pardhu,Length
# Pardhu("john")
# 
# print(Length([1,2,34,4]))


import gen as Files

print(Files.Length([1,2,3,4,5,4,4]))

from gen import Pardhu as p
print(p("john"))








