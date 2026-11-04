'''
file=open("pardhu.txt",mode="a")
file.write("\ni am good how are you")
print("sucess")
file.close()


file=open("pardhu.txt","r")
print(file.readlines())

#x -->to create
f=open("babu.txt","x")
f.write("python inserting info")
print("success")
f.close()
'''


#w+ -->write+read
'''
#r+ ---->read+write  content add at the beginning:
with open("babu.txt","r+") as file:
    file.write("hello how are you")
    print("success")
    print(file.tell())
    file.seek(0)
    print(file.read())
'''

    
    
#csv -->comma seprated values:
'''
with open("transaction.csv","a") as file:
    file.write("lasya,23,100000\n")
    print("success")

'''












