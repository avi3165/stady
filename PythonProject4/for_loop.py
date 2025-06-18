# q1
# nums=[1,4,4,3]
# for number in range(len(nums)):
#     print(nums[number])
#q2
# name="avi"
# for a in range(100):
#     print(name)
#q3
# user_name=input("Please enter your name: ")
# for x in range(1,101):
#     print(user_name,x)
#q4
# for number in range(1,101):
#     if number%3==0:
#         print(number)
#q5
# for number in range(1,1001):
#     if number%3==0 and number%5==0:
#         print(number)
#q6
# for num in range(1,101):
#     if num%7==0:
#         print(num)
#     elif num%9==0:
#         print(num)
#q7
# for num in range(1,6):
#     print(str(num)*5)
#q8
number = int(input("Please enter a negative number:"))
if number>=0:
    number = int(input("The number you gave is positive. \nPlease enter a negative number:"))
for num in range(number, 1):
        print(num)
