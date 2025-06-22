#q1
# list_1=[5,-2,100,-3,-6,-4,2,111]
# h=l[:]
# a=[]
# for i in range(1,len(list_1)+1):
#     for c in range(len(list_1)):
#         a=list_1[c:c+i]
#         if sum(a)>sum(h):
#             h=a
# print(h)
#q2
def Magen_David(h,d):
    r=" "
    s=h+d
    w=h*2-1
    help_1 = 0
    help_2=0
    First_triangle=1
    second_triangle=s*2-1
    for i in range(s):

        #שפיץ עליון ושפיץ תחתון
        if i == 0 or i == s-1:
            print(r * ((w - 1) // 2)+"/")

        #קו תחתון משולש עליון או קו עליון משולש תחתון
        elif i==h-1 or i==d:
            print("/"*w)

        #  אמצע ומשפיץ עליון עד לקו עליון של משולש תחתון
        elif i==s//2 or (i>0 and i<d):
            if i==s//2 and s%2==0:
                help_2 = First_triangle-4
                help_1 = int((w - ((w - second_triangle+2) // 2) *2 - help_2 - 4) / 2)
                print(r * ((w - second_triangle-1) // 2)+ "/" + help_1*r + "/" + r * (First_triangle-4) + "/" + help_1*r + "/")
            else:
                print(r * ((w - First_triangle) // 2)+"/"+ r * (First_triangle-2) +"/")

            #   משפיץ תחתון ועד לקו תחתון של משולש עליון
        elif  i >=h and i <s-1:
            print(r * ((w - second_triangle) // 2) + "/" + r *(second_triangle-2) + "/")

            #מקו עליון משולש תחתון ועד האמצע
        elif  i<(s)//2 and  i>d:
            help_2=First_triangle - 2
            help_1 = int((w-((w - second_triangle) // 2)*2-help_2-4)/2)
            print(r * ((w - second_triangle) // 2)+ "/" + r*help_1 + "/"+ r* (First_triangle-2) + "/" + r*help_1 + "/")

            #מהאמצע ועד קו תחתון משולש עליון
        elif  i>(s)//2 and  i<h:
            help_2 = second_triangle - 2
            help_1 = int((w-((w - First_triangle) // 2)*2-help_2-4)/2)
            print(r * ((w - First_triangle) // 2)+ "/" + help_1*r + "/"+ r* (second_triangle - 2) + "/" + help_1*r + "/")
        First_triangle+=2
        second_triangle-=2
h=int(input("enter height number: "))
d=int(input("enter distance number: "))
Magen_David(h,d)


