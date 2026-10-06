#set:
'''n=set({50,10,1,2,20,3,4,5,1,1,1,1,1,1,1})
print(type(n))
print(n)


x={1,1,1,12,3,1,}
print(x)

x={True,1}
print(x)
'''


'''
#to add single element
s=set({1,2,3,4,5})
s.add(20)
print(s)

#update --> one or more elements
s.update({9,6})
print(s)

#pop:
print(s.pop())
print(s)

#discard:
s.discard(20)
print(s)


#remove:
#s.remove(1000)
print(s)


s.clear()
print(s)

del s
print(s)

'''


#
##babu={"phani","sai","john","ram"}
##ntr={"pardhu","john","ram","kumar"}

#union-->all
##print(babu.union(ntr))
##print(ntr | babu)

#intersection -->commom
##print(babu.intersection(ntr))
##print(ntr & babu)


#difference --> only one side
##print(babu.difference(ntr))
##
##print(ntr - babu)

#symmetric_difference:
'''
print(babu.symmetric_difference(ntr))

print(ntr ^ babu)'''


#subset: x all elements must in y
'''
x={1,2,3}
y={1,2,3,4,4,}
print(x.issubset(y))
print(y<x)
'''

#superset:
'''
x={1,2,3,4}
y={1,2,3,4,5}
print(x.issuperset(y))
print(y >= x)
'''


#isdisjoint:  NO common elements
'''
n={1,2,3}
m={4,5,6,2}
print(n.isdisjoint(m))
'''

#python built-in:
##s={1,2,3,4,5,6}
##
##print(max(s),min(s),len(s),sum(s))
##print(sorted(s))
##print(s)


#set operations:
##n={1,2,3}
##m={1,2,3}
##print(n==m)


#list operations:
##l=[1,2,3,4]
##m=[1,2,3,4]
##print(l+m)
##
##print(m>=l)
##print(l==m)

#print("z">"ab")




#user_inputs:

#list:
#int-->
#1,2,3,4,5--->[1,2,3,4,5]
##n=set(map(float,input("enter values:").split(":")))
##print(n)

'''
n=list(input().split(" "))
print(n)'''

n=6
l=list(map(int,input().split()))[:n]
print(l)








