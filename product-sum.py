def productsum(arr,l,s):
    for i in arr:
        if type(i) is list:
            s+=productsum(i,l+1,0)
        else:
            s+=i
    return s*l
    
    
arr=[5,2,[7,-1],3,[6,[-13,8],4]]
print(productsum(arr,1,0))