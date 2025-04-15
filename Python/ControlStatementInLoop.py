# Control Statement: -

# 1: Break:-

studentData=[20,50,25,60,10,65]

##for loop
for data in studentData:   #60
    print(data)            #20 50 25 60
    if data == 60:          #60 == 60
        break


##while loop
print("-------------------")

num=1
while num<11:
    print(num)
    if num==5:
        break
    num+=1


#Example 2

print("-------num even number from 30 to 5------------")
num=30
while num>5:
    print(num)
    if num==14:
        break
    num=num-2


print("------------------")
num=30
while num>5:
    if num==14:
        break
    print(num)
    num=num-2
