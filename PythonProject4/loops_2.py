#q1
# for c in range(1,1001):
#     if c%15==0:
#         print("FuzzBuzz")
#     elif c%5==0:
#         print("Buzz")
#     elif c%3==0:
#         print("Fuzz")
#     else:
#         print(c)
#q2
# a=0
# b=int(input("Please enter a number: "))
# while a<b:
#     a += 1
#     print("*"*a)
# while a>0:
#     a-=1
#     print("*"*a)
#q3
# a=int(input("Please enter a number:"))
# for i in range(2,a):
#     if a%i==0:
#         print("It is not a first number")
#         break
#     elif i==a-1:
#         print("It is a first number")
#q4
# num=int(input("Please enter a number: "))
# for c in range(1,num+1):
#     if c<10:
#         b=str(c)+" "
#     else:
#         b=str(c)
#     a=num-c
#     print(" "*a,c*b)
#q5
# number=input("Please enter a number: ")
# a=number[::-1]
# if number==a:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")
#q6
# b=0
# numberS=[]
# even_numbers=[]
# odd_numbers=[]
# e=0
# while True:
#     number = input("please enter a number: ")
#     if number == "exit":
#         if len(numberS) == 0:
#             continue
#         else:
#             break
#     else:
#         number = int(number)
#         numberS.append(number)
#         if number%2==0:
#             even_numbers.append(number)
#         else:
#             odd_numbers.append(number)
#     b+= number
#     e+=1
# choose=input("Choose from the list\na.Show how much numbers you enter\nb.Show the sum\nc.Show even and odd numbers\nd.Show max and min number\ne.Show average\n")
# if choose=="a":
#     print(len(numberS))
# elif choose=="b":
#     print(b)
# elif choose=="c":
#     print("even numbers:",len(even_numbers),"\nodd numbers:",len(odd_numbers))
# elif choose=="d":
#     print("the max number:",max(numberS),"\nthe min number:",min(numberS))
# elif choose=="e":
#     print(b/e)
#q7
# users={}
# massage="hello men!"
# while True:
#     enter_1 = input("a. enter to the system\nb. make new user\nc. exit from the system\n")
#     if enter_1=="a":
#         name=input("enter user name:")
#         if name in users.keys():
#             for c in range(3):
#                 password=input("enter password:")
#                 if users[name]==password:
#                     options=input("a.print\nb.change password\nc.delete user\nd.return to main menu\ne.exit from the system\n")
#                     if options=="a":
#                         print(massage)
#                     elif options=="b":
#                         change_password=input("enter a new password")
#                         users[name]=change_password
#                     elif options=="c":
#                         users.pop(name)
#                     elif options=="d" or "*":
#                         break
#                     elif options=="e":
#                         exit()
#                 elif password=="*":
#                     break
#         else:
#             print("user don't pound")
#             continue
#     elif enter_1=="b":
#         new_user_name=input("enter your user name:")
#         new_user_password=input("enter a password")
#         if new_user_name == "*" or new_user_password == "*":
#             continue
#         users[new_user_name]=new_user_password
#         continue
#     elif enter_1=="c":
#         break
#q8
num=int(input("Please enter a number:"))
su=[]
a=1
for c in range(num):
    if len(su)==1:
        su.append(1)
    else:
        su.append(a)
    a=su[c-1]+su[c]
    print(su[c],end=" ")
print(" ")
print("the sum of all numbers is:",sum(su))