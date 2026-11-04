'''
a=10
try:
    print(a)
    print(a/2)
    
    l=[1,2,3]
    print(l[0])
    
    d={1:"a",2:"b"}
    print(d[2])
    
    x="n"
    print(x+"x")
    
    n=list(map(int,input().split()))
    print(n5)
    

except NameError:
    print("variable not exists")
    
except ZeroDivisionError:
    print("you cannot divisible by 0")
    
except IndexError:
    print("values should be in range")
    
except KeyError:
    print("try to use existing info")
    
except TypeError:
    print("you cannot add differnt datatypes")
    

except ValueError:
    print("please check the data type")
    
else:
    print("done")
    
finally:
    print("completed")
    '''
a=10
try:
    print(a)
    print(a/2)
    
    l=[1,2,3]
    print(l[0])
    
    d={1:"a",2:"b"}
    print(d[2])
    
    x="n"
    print(x+10)

 
except Exception as error:
    print(error)
    

'''
import os
def create_file(file):
    try:
        os.mkdir(file)
    
    except FileExistsError:
        print("file already exists")
    else:
        print("file created succesfullly")
    
    
def Path():
    print(os.getcwd())
    
    
def Delet(file):
    try:
        os.rmdir(file)
        
    finally:
        print("completed")
 
while True:
    n=int(input("1.Createfile\n2.path\n3.Delete file:"))
    if n==1:
        file=input()
        create_file(file)
    elif n==2:
        Path()
    elif n==3:
        file=input("enter remove file name:")
        Delet(file)

'''
















