'''
def Hello():
    print("hii")
    
    Hello()
    
Hello()
'''

'''
def Number(n):
    if n==10:
        return "hello"
    
    else:
        print(n)
        print(Number(n+1))
       
Number(1)
'''


#factorial
'''
def Fact(n):
    if n==5:
        return 5
    
    else:
        return n*Fact(n+1)
        
print(Fact(1))
'''

'''
def Fibonacci(a,b,n):
    i=0
    while i <=n:
        print(b, end=" ")
        
        temp=a
        a=b
        b= b+temp
        i+=1
    
n=int(input())
a=0
b=1
Fibonacci(a,b,n)
'''

def Fib(n):
    if n<=1:
        return n
    else:
       return Fib(n-1)+Fib(n-2)
    
# for i in range(5):
#     print(Fib(i))
print(Fib(6))








