def function(arr,comb,start,k):
	if len(comb) == k:
		print(comb)
		return
	if start == len(arr):
		return
	for i in range(start,len(arr)):
		comb.append(arr[i])
		function(arr,comb,i+1,k)
		comb.remove(arr[i])

function([2,3,5,8],[],0,3)