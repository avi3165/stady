
# #q1
# list_1=[5,-2,100,-3,-6,-4,2,111]
# h=[]
# a=[]
# for i in range(1,len(list_1)+1):
#     for c in range(len(list_1)):
#         a=list_1[c:c+i]
#         if sum(a)>sum(h):
#             h=a
# print(h)
#q2
a=0
f=1
first_number=int(input("first number"))
second_number=int(input("second number"))
e=first_number-2
b=second_number*2-1
for c in range(1,first_number+second_number+1):
    if c==first_number+second_number or c==1:
        print(" "*(first_number-1)+"/")
    elif c==first_number or c==second_number+1:
        print("/" *( (first_number * 2)-1))
    elif c==(first_number+second_number)//2+1:
        print(" "*(second_number),"/"," "*(first_number),"/")
    elif c>second_number and c<(first_number+second_number)//2+1:
        print(" "*(a+1)+"/"+" "*b+"/"+" "*((first_number//2+2)+(a*2))+"/"+" "*(b)+"/")
        a+=1
        b-=2
    elif c<first_number and c>(first_number+second_number)//2+1:
        print(" " * (a) + "/" + " " * (b+2) + "/" + " " * ((first_number // 2 ) + (a * 2)) + "/" + " " * (b+2) + "/")
        a-=1
        b+=2
    elif 1<c<second_number+1:
        print(" "*e+"/"+" "*f+"/")
        f+=2
        e-=1
    elif first_number<c<first_number+second_number+1:
        print(" " * (e+1) + "/" + " " * (f-2) + "/")
        f -= 2
        e += 1



