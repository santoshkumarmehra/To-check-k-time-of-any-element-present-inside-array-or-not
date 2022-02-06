def findk(arr,k):
	s=set(arr)           #using set 
	for ele in arr:
		if ele*k in s:   #searching element in set
			return True
	return False

arr=[5,4,6,8,3,9]
k=2
result=findk(arr,k)
print(result)