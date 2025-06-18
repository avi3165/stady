#q1
# def hello_world():
#     print("Hello world")
# hello_world()
#q2
# def sum_multiplication(a,b):
#     sum_1=a+b
#     multiplication=a*b
#     return "the sum is", sum_1,"the multiplication us", multiplication
# print(sum_multiplication(2,3))
#q3
# def sum_multiplication_list(a,b):
#     list_1=[]
#     sum_1=a+b
#     list_1.append(sum_1)
#     multiplication=a*b
#     list_1.append(multiplication)
#     return list_1
# print(sum_multiplication_list(3,5))
#q4
# def even(a):
#     even=False
#     if a%2==0:
#         even=True
#     return even
# print(even(9))
#q5
# def tree_strings_to_string(a,b,c):
#     string_1=a
#     string_2=b
#     string_3=c
#     string_4=a+b+c
#     return string_4
# print(tree_strings_to_string("my ","name ","is"))
#q6
def reverse_world(a):
    new_world=a[::-1]
    return new_world
print(reverse_world("hello"))