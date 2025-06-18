#q1
# day=input("What day is today:")
# simple_day=["sunday","monday","tuesday","wednesday","thursday"]
# fri="friday"
# shabat="saturday"
# if day==fri:
#     print("are you ready to shabat kodesh?")
# elif day==shabat:
#     print("What a wonderful day!")
# else:
#     print("it's a day to study a new thing")
#q2
# menu="Menu:\nA.Black Coffee\nB.Chocolate\nC.Ness Coffee"
# print(menu)
# order=input("Please choose a drink from our menu:")
# if order=='a':
#     print("Your Black Coffee is in the way\nThank you!")
# elif order=='b':
#     print("Your Chocolate is in the way\nThank you!")
# elif order=='c':
#     print("Your Ness Coffee is in the way\nThank you!")
# else:
#     print("rong answer\nplease choos a letter from the list")
#q3
# num_1=int(input("Please enter the first number:"))
# oper=input("Please enter a operator:")
# num_2=int(input("Please enter the second number:"))
# op1="+"
# op2="-"
# op3="*"
# op4="/"
# op5="%"
# op6="**"
# if oper==op1:
#     print(num_1+num_2)
# elif oper==op2:
#     print(num_1-num_2)
# elif oper==op3:
#     print(num_1*num_2)
# elif oper==op4:
#     print(num_1/num_2)
# elif oper==op5:
#     print(num_1%num_2)
# elif oper==op6:
#     print(num_1**num_2)
# else:
#     print("rong answer\nPlease check your answers")
#q4
# year=int(input("Please enter the number of days "))
# if year%4==0:
#     if year%100==0:
#         if year%400:
#             print("This year is leap")
# else:
#     print("This year isn't leap")
#q5
# num_1=int(input("Please enter your first number:"))
# num_2=int(input("Please enter your second number:"))
# num_3=int(input("Please enter your third number:"))
# if num_1>num_2 and num_1>num_3 and num_2>num_3:
#     print("Your numbers are going down")
# elif num_1<num_2 and num_1<num_3 and num_2<num_3:
#     print("your set is going up")
# else:
#     print("Your set without any order")
#q6
# age=int(input("Please enter your agg:"))
# weight=int(input("Please enter your weight:"))
# height=int(input("Please enter your height:"))
# ratio=height/weight
# if age>=11 and age<=120 and ratio>=0.5 and ratio<=2 or age>=21 and age<=40 and ratio>3.5 and ratio<=5:
#     print("A-Menu")
# elif age>=11 and age<=40 and ratio>2 and ratio<= 3.5:
#     print("B-Menu")
# elif (age>=11 and age<=20 or age>=41 and age<=120) and ratio>3.5 and ratio<=5 or age>=41 and age<=120 and ratio>2 and ratio<=5:
#     print("C-Menu")
# else:
#     print("Sorry, we dont have any menu for you.")
#q7
Round_down=1
Round_up=2
Round=3
choose=int(input("Please choose for this list one number: \nFloor round-1 \nCeiling round-2 \nRound to the nearest whole number-3: "))
num=float(input("Please enter a float number:"))
if choose==1:
    print("Your number is :",int(num))
elif choose==2:
    num+=1
    print("Your number is:",int(num))
elif choose==3:
    print("Your number is:", round(num))
else:
    print("Rong answer please try again!")
