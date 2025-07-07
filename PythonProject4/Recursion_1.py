#q1
# def func1():
#     a=1
#     return func1()
# func1()
#q2
# def plus(n):
#     print(n)
#     return plus(n+1)
# print(plus(2))
#q3
# def str_1(st:str):
#     print(st)
#     return str_1(st[:-1])
# print(str_1("avraham"))
#q4
# def call_me(num:int):
#     if num==0:
#         return
#     else:
#         print("call")
#         call_me(num-1)
# call_me(4)
#q5
# def num_to_zero(num:int):
#     if num==0:
#         return
#     print(num)
#     num_to_zero(num-1)
# num_to_zero(6)
#q6
# def my_chair(chair:int,ans=0):
#     if chair==0:
#         return ans
#     else:
#         return my_chair(chair-1,ans+1)
# print(my_chair(7,0))
#q7a
# def revers(num:int):
#     if num<10:
#         print(num)
#     else:
#         digit=num%10
#         print(digit,end="")
#         r=num//10
#         revers(r)
# revers(12345)
#q7b
# def broken_revers(num:int):
#     if num<10:
#         print(num,end="")
#     else:
#         digit=num%10
#         r=num//10
#         broken_revers(r)
#         print(digit,end="")
# broken_revers(12345)
#q8a
# def str_reverse(st:str):
#     if len(st)==1:
#         print(st)
#     else:
#         c=st[-1]
#         print(c,end="")
#         r=st[:-1]
#         str_reverse(r)
# str_reverse("avicohen")
#q8b
# def broken_str(st:str):
#     if len(st) == 1:
#         print(st,end="")
#     else:
#         c = st[-1]
#         r = st[:-1]
#         broken_str(r)
#         print(c, end="")
# broken_str("avicohen")
#9
# def factorial(num:int):
#     if num==1:
#         return 1
#     return num*factorial(num-1)
# print(factorial(5))
#10
def fibonacci_numbers(num:int):
    if num<=1:
        return num
    else:
        return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)
print(fibonacci_numbers(100))