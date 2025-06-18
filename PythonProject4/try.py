a=0
f=1
first_number=int(input("first number: "))
second_number=int(input("second number: "))
e=first_number-2
d=first_number+second_number
b=first_number//2
g=0
for c in range(1,d+1):
    if first_number==8 and second_number==3 and  (c == d // 2 or c==d//2+2):
        print(" " + "/" + " " + "/" + " " * (d - 4) + "/" + " " + "/")
    elif c== d or c==1:
        print(" "*(first_number-1)+"/")
    elif c==first_number or c==second_number+1:
        print("/" *( (first_number * 2)-1))
    elif c==d//2+1:
        print(" "*((first_number-second_number)//2)+"/"+" "*(d-2)+"/")
    # elif c == (first_number + second_number) // 2 or c==(first_number+second_number)//2+2:
    #     print(" "+"/"+" "+"/"+" "*(first_number+second_number-4)+"/"+" "+"/")
    elif c>second_number and c<d//2+1:
        a += 1

        print(" "*(a)+"/"+" "*(b)+"/"+" "*((first_number//2)+(a*2))+"/"+" "*(b)+"/")
        b -= 2

    elif c<first_number and c>d//2+1:
        b += 2
        print(" " * (a) + "/" + " " * (b) + "/" + " " * ((first_number // 2 ) + (a * 2)) + "/" + " " * (b) + "/")
        a-=1
    elif 1<c<second_number+1:
        print(" "*e+"/"+" "*f+"/")
        f+=2
        e-=1
    elif first_number<c<d+1:
        print(" " * (e+1) + "/" + " " * (f-2) + "/")
        f -= 2
        e += 1