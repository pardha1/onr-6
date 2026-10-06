#conditional_2:
'''n=input()
if n.isupper():
    print("allow")
else:
    print("no")
'''

##n="hEllO"
##print(n.swapcase())

'''
n=int(input())
if n+10%2==0:
    print("even")
else:
    print("odd")
'''

#leap year:
'''
year=int(input())
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not")
'''
#cars needed:
'''
customers=int(input())
if customers%4==0:
    print(customers//4)
else:
    print(customers//4+1)

'''





#if ,elif,else

'''
n=int(input())
if n==0:
    print("zero")
if n>0:
    print("positive")
else:
    print("negative")
'''

#password strength:
'''
pwd=input()
l=len(pwd)
if l==8:
    print("weak")
elif l>8 and l<16:
    print("good")
elif l>15 and l<=20:
    print("excellent")
elif l>20:
    print("hard to remember")
else:
    print("not valid")
    '''

#nested:

'''
username=input()
if username=="john":
    password=input()
    if password=="1235":
        print("login")
    else:
        print("wrong password")
else:
    print("wrong username")
'''




#nested find std eligiblity:


year=int(input("must be in [1,2,3,4]:"))
if year==4:
    marks=int(input("enter marks:"))
    
    if marks>80 and marks<=100:
        backlogs=int(input("enter bakclogs:"))
        
        if backlogs!=0:
            if backlogs>=1 and backlogs<=3:
                
                pay=input("you have to pay 5000 extra: [yes (or) no]:")
                if pay=="yes":
                    print("eligible for training")
                else:
                    print("must need to pay")

            elif backlogs>3:
                
                pay=input("you have to pay 10k [yes (or) no]:")
                if pay=="yes":
                    print("eligible for trainig")
                else:
                    print("must need to pay 10k")
                    
            
        else:
            print("eligbile for training")

    else:
        print("marks must greater than 80")
else:
    print("year must be 4")
'''
    
            
        
        
    





