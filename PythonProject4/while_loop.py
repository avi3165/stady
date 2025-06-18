#q1
# x=0
# while x<1000:
#     print("avi")
#     x+=1
#q2
# name=input("please enter your name: ")
# x=0
# while x<100:
#     x+=1
#     print(name,x)
#q3
# x=0
# while x<99:
#     x+=3
#     print(x)
#q4
# x=0
# while x>=0:
#     num=int(input("Please enter a number: "))
#     if num ==0:
#         break
#     else:
#         x+=num
# print(x)
#q5
# acc=0
# while 1==1:
#     num=int(input("please enter a number:"))
#     if num==-1:
#         break
#     else:
#         acc+=1
# print(acc)

# acc=0
# while acc!=-1:
#     num=int(input("please enter a number:"))
#     if num==-1:
#         break
#     else:
#         acc+=1
# print(acc)
#q6
# x=0
# while x<1000:
#     x+=1
#     if x%7==0:
#         print("BOOM")
#     else:
#         print(x)
#q7
num=int(input("Please enter a negative number:"))
while num>=0:
    num=int(input("The number you gave is positive, try again:"))
while num<0:
    print(num)
    num+=1
print(num)