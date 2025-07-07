def binary(l,n):
    low=0
    high=len(l)-1
    while low <= high:
        mid=(low+high)//2
        if l[mid]==n:
            return mid
        elif l[mid]< n :
            low= mid+1
        else:
            high= mid-1
    return "not found"
