# for a in range(1,11):
#     print(a,end="  ")
#     if a== 10:
#         print(" ")
# for b in range(1,11):
#     print(b*2,end=" ")
#     if b == 10:
#         print(" ")
# for c in range(1,11):
#     print(c*3,end=" ")
#     if c == 10:
#         print(" ")
# for d in range(1,11):
#     print(d*4,end=" ")
#     if d == 10:
#         print(" ")
# for e in range(1,11):
#     print(e*5,end=" ")
#     if e == 10:
#         print(" ")
# for f in range(1,11):
#     print(f*6,end=" ")
#     if f==10:
#         print(" ")
# for h in range(1,11):
#     print(h*7,end=" ")
#     if h == 10:
#         print(" ")
# for i in range(1,11):
#     print(i*8,end=" ")
#     if i == 10:
#         print(" ")
# for j in range(1,11):
#    print(j*9,end=" ")
#    if j == 10:
#        print(" ")
# for k in range(1,11):
#     print(k*10,end=" ")
# l=["a","b","c","d"]
# for idx,it in enumerate(l):
#     print(idx,it)
# number=input("enter a number with seven digits: ")
# for num in range(len(number)):
#     print("digit",num+1,number[num])
# my_dict={"one":1,"two":2,"three":3,"four":4}
# x = len(my_dict)
# key_dict=list(my_dict.keys())
# value_dict=list(my_dict.values())
# my_list = []
# for i in range(x):
#     my_list.append(value_dict[i])
#     my_list.append(key_dict[i])
# d = {}
# for i in range(0,len(my_list),2):
#     d[my_list[i]] = my_list[i+1]
# print(d)
# d = {}
# for k,v in my_dict.items():
#     if v not in d:
#         d[v] = [k]
#     d[v].append(k)
# print(d)
# x=0
# while x<10:
#     x+=1
#     print(x)
a=[2,4,6,8]
for d in range(2):
    b=a[2-d]+a[d]
print(b)

