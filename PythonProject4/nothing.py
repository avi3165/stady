def find_min_index(l:list[int]):
    min_value=l[0]
    min_index=0
    for i,v in enumerate(l):
        if v<min_value:
            min_value=v
            min_index=i
    return min_index
def swap(l:list[int],a:int,b:int):
    l[a],l[b]=l[b],l[a]
    return l
def selection_sort(l:list[int]):
    for i in range(len(l)):
        m = find_min_index(l[i:])
        swap(l,i,m+i)
    return l
print(selection_sort([89,1,3,7,24]))