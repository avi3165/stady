#q1
# d={"one":1,"two":2,"three":3,"four":3}
# t = {}
# for key,value in d.items():
#     if value in t:
#         t[value].append(key)
#     else:
#         t[value]=[key]
# print(t)
#q2
# d1={"david":"levkovich","idan":"sananes","ahiya":"biton"}
# d2={"ron":"ben yosef","hagay":"kohelet","david":"cohen"}
# d3 = {}
# for k, v in d1.items():
#     d3[k] = [v]
#
# for k,v in d2.items():
#     if k in d3:
#         d3[k].append(v)
#     else:
#         d3[k]=[v]
# print(d3)
#q3
d1={"david":"levkovich","idan":"sananes","ahiya":"biton"}
# l1=[]
# for i in d1.items():
#     l1.append(list(i))
# print(l1)
t1=tuple(d1.items())
print(t1)




