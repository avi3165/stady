#q1
# d={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10}
# for c in d.values():
#     print(c)
# t=(1,2,3,4,5,6,7,8,9,10)
# for c in t:
#     print(c)
#q2
# dict_1={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":34,"l":90,"m":7,"n":8,"o":2,"p":52,"q":46,"r":44,"s":7,"t":77,"u":2,"v":28,"w":21,"x":43,"z":15,"aa":13,"bb":22,"cc":44,"dd":55}
# a=list(dict_1.keys())
# for i in range(1,len(a)):
#     if dict_1[a[i]]%2==0:
#         print(f"{a[i]}:{dict_1[a[i]]}")
#q3
# dict_2={"a":1,"b":2,"c":3,"d":4,"e":5}
# l1=list(dict_2.keys())
# l2=list(dict_2.values())
# dict_3 = {l2[0]:l1[0] , l2[1]:l1[1] ,l2[2]:l1[2] ,l2[3]:l1[3] ,l2[4]:l1[4] }
# print(dict_3)
#q4
# a=input("Please enter string with 20 letters: ")
# dict_4={}
# for i in a:
#     if i not in dict_4:
#         dict_4[i]=1
#     else:
#         dict_4[i]+=1
# print(dict_4)
#q5
# b=int(input("Please enter a number with a lot of digits: "))
# num={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
# while b>0:
#     c=b%10
#     num[c]+=1
#     b=b//10
# print(num)
#q6
# a=[(1,5,3),(5,4,3,2,1),(10,20)]
# for i in range(len(a)):
#     a[i]=list(a[i])
# print(a)
# q7
new_str=input("Please enter a string with symbols and numbers: ")
dict_6={"number":{"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0},"symbol":{"!":0,"@":0,"#":0,"$":0,"%":0,"^":0,"&":0,"*":0,"(":0,")":0}}
for i in new_str:
    if i in dict_6["number"].keys():
        dict_6["number"][i]+=1
    elif i in dict_6["symbol"].keys():
        dict_6["symbol"][i]+=1
new_str = new_str.split()
for i in new_str:
        if i not in dict_6.keys():
            dict_6[i]= 1
        else:
            dict_6[i]+=1
print(dict_6)
#q8
# dict_7={"first_dict":{"a":1,"b":10},"second_dict":{"c":1000,"d":-500,"e":0},"third_dict":{"f":200}}
# a=0
# for i in dict_7.keys():
#     for k,v in dict_7[i].items():
#         if v>a:
#             a=v
#             b=k
#     print(b,end=" ")
#     a=0
# print("Keys of max values")
# r=9999
# for i in dict_7.keys():
#     for k,v in dict_7[i].items():
#         if v<r:
#             r=v
#             b=k
#     print(b,end=" ")
#     r=9999
# print("Keys of min values")
# for i in dict_7.keys():
#     for k,v in dict_7[i].items():
#         if v>=a:
#             a=v
#             b=k
# print(b,end=" ")
# print("Keys of max values")
# r=9999
# for i in dict_7.keys():
#     for k,v in dict_7[i].items():
#         if v<r:
#             r=v
#             b=k
# print(b,end=" ")
# print("Keys of min values")
# a=0
# for i in dict_7.keys():
#     for k,v in dict_7[i].items():
#         a+=v
# print("the sum of all digits: ", a)