'''
def Score_board(overs):
    l=[];start=1
    while start<=overs:
        balls=1
        while balls<=6:
            ball_score=input(f"enter over {start} ball:{balls}:")
            if ball_score=="wd" or ball_score=="nb":
                l.append(1)
                continue
            else:
                l.append(ball_score)
                balls+=1
        print(l)
        start+=1
    
Score_board(2)
'''





# x=[1,2,3,4,5,6]
# print(len(x))


# def Length(x):
#     count=0
#     for i in x:
#         count+=1
#     return count
#         
# 
# def Pardhu(n):
#     print(n.upper())
#     
    
    
        
        



'''
def Addition(x,y):
    print(x+y)
    print(x-y)
    
Addition(10,20)


#anonymous functions:
add=lambda x,y:x-y,x+y
print(add(10,20))
'''

'''
print((lambda x,y:x+y)(10,20))

result=lambda x,y,z,n:[x,y,z,n]
print(result("python","cython","java","bava"))

'''


#print((lambda x:"even" if x%2==0 else "odd")(10))

#print((lambda x:x%2==0 "even")(12))   #error
#if is condatory whern you use if else if mandatory


'''def Find(n):
    if n%2==0:
        if n>5:
            print("positive")
        else:
            print("not")
    elif n%2!=0:
        print("odd")
    
    
Find(10)'''


#print((lambda n:"even" if n%2==0 and n>5 else "odd" if  n%2!=0 else "not")(2))


print((lambda n:[i for i in range(n)])(5)) 


x=[7,8,9,1,2,3,4]
l=[]
for i in x:
    if i%2==0:
        l.append(i)
    else:
        l.append("odd")
print(l)

print([i for i in x if i%2==0])


x=[7,8,9,1,2,3,4]
print({i:"even" if i%2==0 else "odd" for i in x})

    

