

def sortArray(myarr):
	"""
	Purpose: sorts an array of only 0s and 1s in O(n)
	Example: sortArray([1,1,0,1]) -> [0,1,1,1]
	"""
	newarr=[None]*len(myarr)
	startIndex=0
	endIndex=len(myarr)-1
	for i in myarr:
		if myarr[i] < 1:
			newarr[startIndex]=0
			startIndex+=1
		else:
			newarr[endIndex]=1
			endIndex-=1
	return newarr


#Test case for the sortArraay method
testArr=[0,1,1,1,1,0,0,0,0]
print(testArr)
print(sortArray(testArr))

#Test case for the sortArraay method
testArr=[1,1,1,1,1]
print(testArr)
print(sortArray(testArr))
