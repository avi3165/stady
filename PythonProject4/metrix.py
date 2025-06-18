a=[1,4,0,2,8]
print(a[3])
print(a[3:5])
print(a[::-1])
a.insert(0,5)
print(a)
#b=a.pop(5)
# print(b)
# a.remove(8)
# print(0 in a)
# print(a.index(0))
b=[a[1],a[2],a[3]]
c=[a[2],a[3],a[2]-1]
d=[a[5],a[4],a[1]]
m=[b,c,d]
print(m[2][1])
M=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(len(M),len(M[0]))
M=M[::-1]
print(M[0][::-1],M[1][::-1],M[2][::-1],M[3][::-1])