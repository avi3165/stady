#q1
# num_1=int(input("Please enter 1st number: "))
# num_2=int(input("Please enter 2nd number: "))
# num_3=int(input("Please enter 3rd number: "))
# num_4=int(input("Please enter 4th number: "))
# num_5=int(input("Please enter 5th number: "))
# list=[num_1,num_2,num_3,num_4,num_5]
# list[2],list[1]=list[1],list[2]
# list[3],list[4]=list[4],list[3]
# print(list)
#q2
# numbers=[]
# numbers.append(2)
# numbers.append(3)
# numbers.append(9)
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
#q3
# numbers=[]
# numbers.append(67)
# numbers.append(68)
# numbers.append(69)
# numbers.append(70)
# numbers.append(71)
# print(numbers[::-1])
#q4
# list=[]
# list.append(int(input("Please add 1st number: ")))
# list.append(int(input("Please add 2nd number: ")))
# list.append(int(input("Please add 3rd number: ")))
# list.append(int(input("Please add 4th number: ")))
# list.append(int(input("Please add 5th number: ")))
# list.append(int(input("Please add 6th number: ")))
# input("push enter:")
# print(list[0])
# input("push enter:")
# print(list[1])
# input("push enter:")
# print(list[2])
# input("push enter:")
# print(list[3])
# input("push enter:")
# print(list[4])
# input("push enter:")
# print(list[5])
#q5
# list=[]
# list.append(int(input("Please add 1st number: ")))
# list.append(int(input("Please add 2nd number: ")))
# list.append(int(input("Please add 3rd number: ")))
# list.append(int(input("Please add 4th number: ")))
# list.append(int(input("Please add 5th number: ")))
# list.append(int(input("Please add 6th number: ")))
# input("push enter")
# if list[0]%2==0:
#     print(list[0])
# input("push enter")
# if list[1]%2==0:
#     print(list[1])
# input("push enter")
# if list[2]%2==0:
#     print(list[2])
# input("push enter")
# if list[3]%2==0:
#     print(list[3])
#     input("push enter")
# elif list[4]%2==0:
#     print(list[4])
#     input("push enter")
# elif list[5]%2==0:
#     print(list[5])
#q6
# list=[]
# list.append(int(input("Please add 1st number: ")))
# list.append(int(input("Please add 2nd number: ")))
# list.append(int(input("Please add 3rd number: ")))
# list.append(int(input("Please add 4th number: ")))
# list.append(int(input("Please add 5th number: ")))
# list.append(int(input("Please add 6th number: ")))
# input("Please press enter")
# print("The first number: ",list[0])
# input("Please press enter")
# print("The second number: ",list[2])
# input("Please press enter")
# print("The third number: ",list[4])
#q7
list=[]
list.append(int(input("Please add 1st number: ")))
list.append(int(input("Please add 2nd number: ")))
list.append(int(input("Please add 3rd number: ")))
list.append(int(input("Please add 4th number: ")))
list.append(int(input("Please add 5th number: ")))
list.append(int(input("Please add 6th number: ")))
a=int(input("choose a number from your list: "))
if a in list:
    print("The number in the list")
    print("the number place is:", list.index(a))
    b=list.index(a)-1
    c=list.index(a)+1
    if b>=0 and c<6:
        print("The next number is: ",list[c])
        print("The number before is: ",list[b])
    elif b<0:
        print("The next number is: ", list[c])
    elif c>=6:
        print("The number before is: ", list[b])
else:
    print("It not in the list")
