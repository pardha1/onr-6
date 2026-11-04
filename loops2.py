#v
'''
for i in range(5):
    for j in range(5+4):
        if i==j or i+j==8:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    '''

#prime number:
'''
n=int(input());count=0
for number in range(1,n):
    for i in range(2,number):
        if number%i==0:
            break
    else:
        count+=number
print(count)'''


'''
n=7
for i in range(1,7,2):
    print((i*".|.").center(21,"-"))
'''
p=4;k="z"
x="abracadabra"
l=list(x)
print(l)
l[p]=k
print("".join(l))

















