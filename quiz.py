import random as r
questions={"what is python?":["1.programming language","2.os","3.data type"],"what is int" : ["1.programming language","2.os","3.data type"], "what is windows":["1.programming language","2.os","3.data type"]}
answers={"what is python?":1,"what is int" : 3, "what is windows":2}
a=list(questions.keys())
r.shuffle(a)
score=0
for i in range(len(a)):
  print(a[i])
  print(questions[a[i]])
  answer=int(input())
  print("your answer is:" ,answer)
  correctanswer=answers[a[i]]
  print(f"correct answer is:{correctanswer}")
  if(answer==correctanswer):
    score+=1
    print("your answer is correct")
  else:
    print("wrong answer")  


print(f"Totalscore={score}/{len(a)}")