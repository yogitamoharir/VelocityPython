# While Loop

# while condition
#     body

print("-----Print num 1 to 5 using while Loop-----")
num=1     #StartNum
while num<6:     #6<6   #endNum
    print(num)    #1 2 3 4 5
    num=num+1     # 1+1=2+1=3+1=4+1=5+1=6  #incr/decr   num +=1


print("-----Print num 15 to 30 using while Loop-----")
num=15
while num<31:           #while num<=30:
    print(num)
    num=num+1           #num +=1

print("-----Print Even num 20 to 30 using while Loop-----")
num=20
while num<31:
    print(num)
    num=num+2       #  num +=2


print("-----Print num 5 to 1 using while Loop-----")
num=5
while num>0:        #while num>=1:
    print(num)
    num=num-1    #  num -=1


print("-----Print Even num from 30 to 22 using while Loop-----")
num=30
while num>=22:        #while num>21:
    print(num)
    num=num-2        #  num -=2


print("---------infinite loop-----------------")
num=1
while num<6:     #-1<6
    print(num)   # 1 0 -1
    # num=num-1   # -2   ##infinite loop
    num=num+1   # -2
