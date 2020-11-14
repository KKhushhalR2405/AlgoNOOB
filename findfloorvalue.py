# iterative solution
def floor(arr,target):
    l=0
    u=len(arr)-1
    n=0
    diff = float("inf")
    
    while l<=u:
        m = (l+u)//2
        if arr[m]==target:
            n = m
            break
        elif arr[m] < target:
            if target - arr[m] < diff:
                n = m
                diff = target - arr[m]
            l = m + 1
        else:
            u = m - 1
    return n
    
#recursive solution
def floorrec(arr,target,n,diff,l,u):
    if l>u:
        return n
    m = (l+u)//2
    if arr[m]==target:
        n = m
        return n
    elif arr[m] < target:
        if target - arr[m] < diff:
            diff = target - arr[m]
            n=m
        return floorrec(arr,target,n,diff,m+1,u)
    else:
        return floorrec(arr,target,n,diff,l,m-1)
        
    return n

#---main---
arr = [10,20,30,40,50]
target = 45
l=0
u=len(arr)-1
n=0
diff = float("inf")

index1 = floor(arr,target)
index2 = floorrec(arr,target,n,diff,l,u)

print(arr[index1],arr[index2])
            