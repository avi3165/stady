#q1
# def palindrome(s:str):
#     """
#     the function nade to
#     check if word is
#     a palindrome or not
#     """
#     n_s=s[::-1]
#     if s==n_s:
#         print(True)
#     else:
#         print(False)
# s=input("Please enter a palindrome ")
# palindrome(s)
#q2
# def num_to_zero(n:int):
#     """
#     :param n:int
#     :return:the sum of the numbers
#      I have from zero to n
#     """
#     global sum_1
#     sum_1=0
#     for i in range(n):
#         sum_1+=i
#     return sum_1
# print(num_to_zero(8))
#q3
# def sum_numbers(num:list[int]):
#     """
#     :param num:list of numbers
#     :return: the sum of all numbers
#     """
#     global sum_2
#     sum_2=0
#     for i in num:
#         sum_2+=i
#     return sum_2
# print(sum_numbers([1,2,3,45]))
#q4
# def numbers_to_star(num:list[int]):
#     """
#     :param num: list of numbers
#     :return: turn the numbers to stars
#     and print them reversed
#     """
#     global n_list
#     n_list=[]
#     for i in num[::-1]:
#         star=i*"*"
#         n_list.append(star)
#     return n_list
# print(numbers_to_star([6,2,3]))
#q5
# def add_number(num_1:int,num_2:int):
#     """
#     the function adding the
#     numbers and return the sum
#     :param num_1:number
#     num_2:number
#     :return: a sum
#     """
#     sum_2=num_1+num_2
#     return sum_2
# def multiplying_numbers(num_1:int,num_2:int):
#     """
#     function
#     :param num_1:integer
#     :param num_2:integer
#     :return: a multiplier
#     """
#     multiplier=num_1*num_2
#     return multiplier
# def my_func(n:int):
#     """
#     the function receives
#     number and return
#     a list with:
#     1.the sum of the number whit his next
#     2.the multiplier of the number whit his next
#     3.the sum of the number and the number before
#     4.the multiplier of the number and the number before
#     :param n:int
#     :return:list
#     """
#     num_1=n
#     num_2=n+1
#     a=add_number(num_1,num_2)
#     m=multiplying_numbers(num_1,num_2)
#     num_2=n-1
#     a_2=add_number(num_1,num_2)
#     m_2=multiplying_numbers(num_1,num_2)
#     my_list=[a,m,a_2,m_2]
#     return my_list
# print(my_func(2))
#q6
# def sum_num(*n1:int):
#     """
#     the function receives numbers
#      and return the sum of them
#     :param n1:int
#     :return: sum
#     """
#     return sum(n1)
# print(sum_num(1,2,3,4,5,6))
#q7
# def even_index(*n:int):
#     """
#     the user enters numbers
#     and get a list only with the
#     even index
#     :param n: ints
#     :return: list
#     """
#     lis_1=[]
#     for i,v in enumerate(n):
#         if i %2==0:
#             lis_1.append(v)
#     return lis_1
# print(even_index(1,2,3,4,4))
#q8
# def Quadratic_equation(a:int,b:int,c:int):
#     """
#     roots formula
#     :param a: Coefficient of X
#     :param b:X
#     :param c:A simple number
#     :return:two x
#     """
#     root=(b ** 2 - 4 * a * c)
#     x_1=(-(b) - (root**0.5)) / (2*a)
#     x_2=(-(b) + (root**0.5)) / (2*a)
#     if root<0:
#         txt="The equation is unsolvable."
#         return txt
#     elif x_1==x_2:
#         return (f"[x={x_1}]")
#     else:
#         return [f"x1={x_1} x2={x_2}"]
# print(Quadratic_equation(1,4,5))
#q9
# def create_dict(**dict:dict[str:int]):
#     """
#     the function made to make dict
#     from input of the user
#     """
#     return dict
# print(create_dict(avi=29 , david=23, ori=22))
