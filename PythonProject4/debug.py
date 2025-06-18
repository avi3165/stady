# def sum_list(numbers):
#     total = 0
#     for num in numbers:
#         total += number
#     return total
# print(sum_list([1, 2, 3, 4]))

#תקלה בשורה 4 אין משתנה בשם
# number
# def concatenate_strings(str_list):
#     result = ""
#     for s in str_list:
#         result += s
#     return resut
# print(concatenate_strings(["Hello", " ", "World!"]))
#the  bug in line 14
def average_list(numbers):
    total = sum(numbers)
    return total / len(numbers)
print(average_list([10, 20, 30, 40]))
print(average_list([]))