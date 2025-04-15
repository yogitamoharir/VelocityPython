# # ****Example 1
# # * * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
# # * * * * * * * * * *
#
# # n=10
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #      print("*",end=" ")
# #     print()
# #
# #
# # # n=10
# # # for i in range(1,n+1):
# # #     for j in range(1,n+1):
# # #      print(i,end=" ")
# # #     print()
# #
# #
# # print("-------------------------------")
# #
# # n=10
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #      print(j,end=" ")
# #     print()
# #
# # print("-------------------------------")
# #
# # n=10
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #       print(chr(64+i),end=" ")
# #     print()
# #
# #
# #
# # n=10
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #       print(chr(64+j),end=" ")
# #     print()
# #
# #
# # n=10
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #       print(n+1-i,end=" ")
# #     print()
# #
# # n=10
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #       print(n+1-j,end=" ")
# #     print()
# #
# # n=10
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #       print(chr(65+n-i), end=" ")
# #     print()
# #
# # n=10
# # for i in range(1,n+1):
# #     for j in range(1,n+1):
# #       print(chr(65+n-j), end=" ")
# #     print()
#
#
#
# """
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *
# """
#
# n=10
# for i in range(1,n+1):
#     for j in range(i):
#       print("*", end=" ")
#     print()
#
# # n=int(input("enter number:- "))
# # print("* "*i)
#
# n=10
# for i in range(1,n+1):   #1, 2
#     for j in range(i):  #1 ,2
#       print(i, end=" ") #1, 22, 333,4444,55555 and so on
#     print()
#
# n=10
# for i in range(1,n+1):
#     for j in range(1,i+1):
#       print(j, end=" ")
#     print()
#
#
# n=10
# for i in range(1,n+1):   #(1,11)x
#     for j in range(1,n+2-i):   #1,(10+2-1)=1,11
#       print("*", end=" ")
#     print()
#
#
# n=10
# for i in range(1,n+1):   #(1,11)x
#     for j in range(1,n+2-i):   #1,(10+2-1)=1,11
#       print(i, end=" ")
#     print()
#
# n=10
# for i in range(1,n+1):   #(1,11)x
#     for j in range(1,n+2-i):   #1,(10+2-1)=(1,2,3...10),(1,2,3..9)
#       print(j, end=" ")
#     print()
#
#
# n=10
# for i in range(1,n+1):
#     for j in range(1,1+i):
#       print("*",end=" ")
#     print()
#


print(type({}))