from binari_search import binari
#1
# def find_element(n:list[int],num:int):
#     a=False
#     for i,v in enumerate(n):
#         if num==v:
#             print("the number found in index",i)
#             a=True
#     if a==False:
#         print("The number did not found ")
# n=[]
# for a in range(5):
#         b=int(input("enter a number:"))
#         n.append(b)
# num=int(input("enter a number to check"))
# find_element(n,num)
#2
# def find_word(li:str,w:str):
#     l=li.split(',')
#     l_1=[]
#     a=False
#     for i in l:
#         l_1.append(i)
#     for i,v in enumerate(l_1):
#         if w == v:
#             print("the word found in index", i)
#             a=True
#     if a==False:
#         print("the word did not found")
# li=input("enter a list: ")
# w=input("enter a word to check: ")
# find_word(li,w)
#3
# def Pair_numbers(n:list[int],num:list[int]):
#     a=False
#     for i in range(len(n)):
#         if num[0]==n[i] and num[1]==n[i+1]:
#             print("the numbers found in the list together")
#             a=True
#     if a==False:
#         print("The numbers did not found together")
# n=[]
# for a in range(5):
#         b=int(input("enter a number:"))
#         n.append(b)
# d=int(input("enter a number to check: "))
# e=int(input("enter a number to check: "))
# num=[d,e]
# Pair_numbers(n,num)
#4
# def in_sorted_matrix(m:list[list[int]],n:int):
#     for i in m:
#
# def in_matrix(m:list,n:int):
#     flag=False
#     for i,v in enumerate(m):
#         for j,h in enumerate(v):
#             if n==h:
#                 print("the number found in: \nline index:",i,"\nin index:",j)
#                 flag=True
#     if not flag:
#         print("not found")
# m=[]
# f_l=input("Please enter first list: ")
# s_l=input("Please enter second list: ")
# t_l=input("Please enter third list: ")
# f_l=f_l.split(",")
# s_l=s_l.split(",")
# t_l=t_l.split(",")
# m.append(f_l)
# m.append(s_l)
# m.append(t_l)
# for i,v in enumerate(m):
#     for j,h in enumerate(v):
#         m[i][j]=int(h)
# n=int(input("please enter a number to check:" ))
# in_matrix(m,n)
#challenge


#5
list_3=[3,7,23,46,89,91,102,122,211]
# def find_num(l:list,n:int):
#     a = False
#     for i,v in enumerate(list_3):
#         if n==v:
#             a=True
#             print("the number found in index",i)
#     if a == False:
#         print("The number was not found")
# #6
# def find_num(l,n):
#     print(l[0])
#     print(l[-1])
#7
# print(binari(list_3,91))
#8
l=[0,0,0,0,0,0,0,1,1,1,1,1,1]
def binari_zero():
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == 0:
            if l[mid+1]==1:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return None
print(binari_zero())