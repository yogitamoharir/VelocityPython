					# Loops

# 1: For Loop

# Example1:
#Print num  from 1 to 5
#StartNum=1
#endNum=5
#incr/decr= bydefault 1

for i in range(1,6):   # 6  ->   6<6                     range(StartNum, endNum+1)
    print(i)            #1 2 3 4 5
    # default incr by 1

print("------------------------")

for i in range(1,6,1):   # 6  ->   6<6                     range(StartNum, endNum+1)
    print(i)            #1 2 3 4 5

print("----------------")
#Print num  from 25 to 50
for i in range(25,51):
    print(i)


# Example2:-

#StartNum=2
#EndNum=8
#incr/decr=incr 2

print("-----print even num 2 to 8-----")
for i in range(2,9,2):     #2+2=4+2=6+2=8+2=10   -> 10<9
    print(i)               # 2 4 6 8

print("----------print even num from 10 to 50----------")
for i in range(10, 51, 2):
    print(i)

print("---------table of 5-----------")
for i in range(5, 51, 5):
    print(i)

print("---------table of 5-----------")
for i in range(1,11):
    print(i*7)

print("---------print square of num from 5 to 10-----------")
for i in range(5,11):   #6    6<11
    print(i*i)   #6*6=36


# Example3:

print("---------print num from 5 to 1----------")
#startNum=5
#end num=1
#incr/decr= decr num by 1

for i in range(5, 0,-1):   #0    0>0 -> true/false  starNum>endNum
    print(i)            #5 4 3 2 1


print("---------print num from 100 to 20----------")
for i in range(100, 19, -1):
    print(i)


print("---------print num from 20 to 15----------")
for i in range(20, 14, -1):
    print(i)



# Example4:

print("---------print Even num from 10 to 2----------")
#startNum=10
#end num=2
#incr/decr= decr num by 2

for i in range(10, 1,-2):   #10-2=8-2=6-2=4-2=2-2=0    0>1 -> true/false  starNum>endNum
    print(i)            #10 8 6 4 2


print("---------print Even num from 100 to 20----------")
for i in range(100, 19,-2):
    print(i)

# Example6:

studentAllData=["Amol", 101, 65.1,'A']

print("------Print all data from list------")
for singleData in studentAllData:
    print(singleData)


print("------Print all data from list in Reversed order------")
for singleData in reversed(studentAllData):
    print(singleData)













