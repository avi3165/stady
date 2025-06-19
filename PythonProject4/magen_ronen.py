def bace(h:int):
    print("/"*(h*2-1))
def kodkod_elion (h:int,d:int):
    print(" "*(h-1)+"/")
    s=1
    for i in range(2,d+1):
        print(" " * (h-i)+"/"+" " * s + "/")
        s+=2

def kodkod_tacton(h:int,d:int):
    s=(d-1)*2+1
    for i in range(d+1,2,-1):
        print(" " * (h - i) + "/" + " " * s + "/")
        s-=2
    print(" " * (h - 1) + "/")
h=8
d=3
print(kodkod_elion(8,3))
print(bace(8))
print(bace(8))
print(kodkod_tacton(8,3))
