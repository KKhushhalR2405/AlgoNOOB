def su(arr,k):
    l=0
    u=len(arr)-1
    s=0
    arr.sort()
    while l<u:
        s=arr[l]+arr[u]
        if s==k:
            return "YES"
        elif s>k:
            u-=1
        else:
            l+=1
    else:
        return "NO"
            
        
print(su([1,6,4,2,11,-1],13))