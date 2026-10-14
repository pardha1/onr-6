#max:
'''
a=1
b=1
c=0
g=s=0

if a>g:
    g=a
    
if b>g:
    s,g=g,b
    
elif b>s and b!=g:
    s=b
    
if c>g:
    s,g=g,c
elif c>s and c!=g:
    s=c

print(g,s)
'''



'''
x=[7,6,4,5,-6]
g=s=float("-inf")
for i in x:
    if i>g:
        s,g=g,i
    elif (i>s and i!=g ) and not(i<s):
        s=i
    
        
    
print(g,s)
'''
        
    
#leets:
'''
n=int(input())
for i in range(65,n+4):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print()
    '''

'''
for i in range(4):
    for j in range(68,68-i-1,-1):
        print(chr(j),end=" ")
    print()
'''

'''
for i in range(68,64,-1):
    for j in range(68,i-1,-1):
        print(chr(j),end=" ")
    print()
'''

for i in range(5):
    for j in range(5):
        if i==2 or j==4 or j==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
            































