#1
# def chr_count(str:str,letter:str,c=0):
#     if len(str)==0:
#         return c
#     else:
#         if letter==str[0]:
#             c+=1
#     s=str[1:]
#     return chr_count(s,letter,c)
#2
# def str_reverse(st:str):
#     if len(st)==1:
#         print(st)
#     else:
#         c=st[-1]
#         print(c,end="")
#         str_reverse(st[:-1])
# str_reverse("avicohen")
#3
# def palin(num:int):
#     if num<10:
#         return True
#     g=num
#     c=0
#     while g>10:
#         g=g//10
#         x = g%10
#         c+=1
#     f=num%10
#     if f!=g:
#         return False
#     return palin(num//10-g*10**(c-1))
# print(palin(12345678765321))
#4
# def count_even(arr,i=0):
#     if len(arr)==0:
#         return i
#     if arr.pop(0)%2==0:
#         i+=1
#     return count_even(arr,i)
# print(count_even([1,2,3,4,5,6,7,8,9,10,11,2,2,2,2]))
# 5
# def is_sorted(arr,i=0):
#     if len(arr) - 1 < i:
#         return True
#     if arr[i]>arr[i+1]:
#         return False
#     return is_sorted(arr,i+1)
# print(is_sorted([1,2,3,4,1,1]))
# def revers(num:int):
#     if num<10:
#         print(num)
#     else:
#         digit=num%10
#         print(digit,end="")
#         r=num//10
#         revers(r)
# revers(12345)
#ariye q3
# def f(n1,n2=0):
#     if n1==n2:
#         return True
#     if n1<n2:
#         return False
#     n2*=10
#     n2+=n1%10
#     if n1==n2:
#         return True
#     return f(n1//10,n2)
# print(f(123211))
#Q6
# def has_negative(arr,i=0):
#     if len(arr)==i:
#         return False
#     if arr[i]<0:
#         return True
#     return has_negative(arr,i+1)
# print(has_negative([1,2,3,4,56,78,934,45,2,332,-23]))
#q7
# def most_common(arr,i=0,max_num=None,max_count=0):
#     if len(arr)==1:
#         return max_num
#     for j in arr:
#         if arr[0]==j:
#             i+=1
#     if i>max_count:
#         max_count=i
#         max_num=arr[0]
#     return most_common(arr[1:],0,max_num,max_count)
# print(most_common([1,23,1,1,1,1,2,33,4,5,56,6,4,4,4,4,4,4,4,3,4,2,2,4,4]))
#q8
# def has_consecutive(arr,i=0):
#     if arr[i]==arr[i+1]-1:
#         return True
#     if i+1==len(arr)-1:
#         return False
#     return has_consecutive(arr,i+1)
# print(has_consecutive([23,43,14,51,12,1]))
#q9
def array_average(arr,i=0,sum1=0,count=0):
    sum1+=arr[i]
    count+=1
    if len(arr)-1==i:
        return sum1/count
    return array_average(arr,i+1,sum1,count)
print(array_average([1,2,3,4,5]))
