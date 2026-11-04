'''
n="python"
for i in range(len(n)):
    for j in range(i+1):
        print(n[j],end="")
    print()
'''

'''
for i in range(5):
    for j in range(5):
        if i%2==0 and j%2==0:
            print("1",end="")
        else:
            print("0",end="")
    print()
'''


'''
i=0
while i<5:
    j=0
    while j<5:
        if i%2==0 and j%2==0:
            print(1,end="")
        else:
            print("0",end="")
        j+=1
    print()
    i+=1
'''


#factorial:

'''
n=5;fact=1
while n>0:
    fact*=n
    n-=1
print(fact)
'''

'''
i=1
n=5
fact=1
while i<=n:
    print(i)
    fact*=i
    i+=1
print(fact)
'''

'''
n=input()

rev=n[::-1]
if n==rev:
    print("palidrome")
else:
    print("not")
    '''


'''n=input()
rev=""
i=0
while i<len(n):
    rev=n[i]+rev
    print(id(rev))
    i+=1
if rev==n:
    print("palidrome")
else:
    print("not a palindrome")
'''

'''
n=121;rev=0
temp=n
while n>0:
    last=n%10
    n=n//10
    rev=rev*10+last  #rev*=10+last

if rev==temp:
    print("plaidnorme")
else:
    print("not")'''


#freq count:
'''
s="abccaaaa"
d={}
i=0
while i<len(s):
    if s[i] in d:
        d[s[i]]+=1
    else:
        d[s[i]]=1
    i+=1
print(d)
'''

'''
d={"pavani":300,"sravya":400,"maheswari":600,"ram":500,"john":700}
highest=0
for key,value in d.items():
    if value>=highest:
        highest=value
for k,v in d.items():
    if v==highest:
        print(k)
'''    




def Login(name,password):
    print(name)
    print(password)
    


name=input("name:")
password=int(input("password:"))
Login(name,password)









