import random
import time
operators=["+","-","*","/"]
rounds=10
wrong=0
listwrong=[]
def generate_problem():
    exp = str(random.randint(2,12)) + random.choice(operators) + str(random.randint(2,12))
    ans = eval(exp)
    return exp, ans
input("\nPress Enter to start")
print('-------------------------------------------------------')
start_time = time.time()
print(start_time)
for i in range(rounds):
    exp, ans = generate_problem()
    print()
    choice= input(f"Question {i}:: {exp} = ")
    if choice!=str(ans):
        wrong+=1
        listwrong.append(i)
end_time = time.time()
print(end_time)
totaltime=round(end_time-start_time,2)
print('-------------------------------------------------------')
print(f"Finished\n Total Time taken to complete is {totaltime}\ntotal wrong {wrong} \nlist of wrong ans {listwrong} ")
    
   