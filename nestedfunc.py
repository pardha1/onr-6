#local vs global
'''
name="codegnan"     #global
def Local():
    #global name
    name="techgnan"
    print(f"{name} local ")
    
Local()

print(f"{name} global")
'''

#nested function:
'''
def Netflix(ruser,pin):
    username=input()
    password=int(input())
    if username==ruser and pin==password:
        def Inside(sub):
            if sub=="yes":
                print("this is inner function")
            else:
                print("no subscription")
            
        sub=input()
        result=Inside(sub)

    else:
        print("not found")
Netflix("john",12345)
'''
    
'''
def Purchase(amount,offer="no"):
    if offer=="yes":
        def Offer(discount):
            return amount-discount
        
        print(Offer(200))
    else:
        print(f"you have to pay {amount}")
        
    
amount=int(input())
offer=input()
Purchase(amount,offer)
'''


#pass by value and pass by refrence:
'''
def Fun(x):
    x.append(99)
    print(x)
    
y=[1,2,3,4]
Fun(y)

print(y)
'''

'''
n=5
a,b=0,1
for i in range(n):
    print(a)
    a,b=b,a+b
'''


def Anagram(s1,s2):
    d1={};d2={}
    if len(s1)==len(s2):
        for i in range(len(s1)):
            if s1[i] not in d1:
                d1[s1[i]]=1
            else:
                d1[s1[i]]+=1
            print(d1)
                
            #word2
            if s2[i] not in d2:
                d2[s2[i]]=1
            else:
                d2[s2[i]]+=1
            print(d2)
              
        print(d1,d2)
        if d1==d2:
            print("anagram")
        else:
            print("not")
                
            
    else:
        print("not a anagram")
                 
    
s1="Heart"
s2="Earth"
Anagram(s1.lower(),s2.lower())
























