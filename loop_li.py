l=[1,3,2,5,7,9,8]
empty=[]
'''
for i in range(len(l)):
    if i%2==0:	
        empty.append(l[i])
print(empty)'''

#evenindex ,odd value:
'''
for i in range(len(l)):
    if i%2==0 and l[i]%2!=0:
        empty.append(l[i])
print(empty)'''

#square of a list:
'''
for i in range(len(l)):
    empty.append(l[i]**2)
print(empty)
'''

#odd vlaues +10:
'''
for i in l:
    if i%2!=0:
        empty.append(i+10)
    else:
        empty.append(i)
print(empty)'''


#revers 1 way:
# l.reverse()
# print(l)


#2 way:
'''
print(l)
for i in range(len(l)-1,-1,-1):
    empty.insert(0,l[i])
    print(empty)
'''

#3-way:
'''
for i in l:
    empty.insert(0,i)
    print(empty)
'''



#find :
'''
names=["mohan","sravya","pavani","babu","lasya"]
search="babu"
for i in names:
    if i==search:
        print("avaialble")
        break
else:
    print("not")
    '''
 
#count_for:
'''
names=["mohan","sravya","pavani","babu","lasya"]
count=[]
for i in names:
    count.append(len(i))
print(count)
    '''

#count while:
'''
names=["mohan","sravya","pavani","babu","lasya"]
i=0;count=[]
while i<len(names):
    count.append(len(names[i]))
    i+=1
print(count)
 '''

#using dict len:
names=["mohan","sravya","pavani","babu","lasya"]
i=0
d={}
while i<len(names):
    d[names[i]]=len(names[i])
    i+=1
print(d)
    
    









































