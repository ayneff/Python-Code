
def mergeSort(myarr):
	"""
	Purpose: sorts an array of integers using the mergesort algorithm
	Example: sortArray([1,10,0,5]) -> [0,1,5,10]
	"""
	if len(myarr) <= 1:
		return myarr
	else:
		pivotIndex=int(len(myarr)/2)
		endIndex=len(myarr)
		return mergeArrays(mergeSort(myarr[0:pivotIndex]),mergeSort(myarr[pivotIndex:endIndex]))

def mergeArrays(arr1,arr2):
	solution=[None]*(len(arr1)+len(arr2))
	arr1Index=0
	arr2Index=0
	i=0
	while arr1Index < len(arr1) and arr2Index < len(arr2):
		if arr1[arr1Index] <= arr2[arr2Index]:
			solution[i]=arr1[arr1Index]
			arr1Index+=1
		else:
			solution[i]=arr2[arr2Index]
			arr2Index+=1
		i+=1

	while arr1Index < len(arr1):
		solution[i]=arr1[arr1Index]
		i+=1
		arr1Index+=1

	while arr2Index < len(arr2):
		solution[i]=arr2[arr2Index]
		i+=1
		arr2Index+=1
	return solution

#Test case with an even number of cells
testArr=[1,4,10,2,-1,-1,50,50,6,3]
print(testArr)
print("starting")
finalAnswer=mergeSort(testArr)
print("done")
print(finalAnswer)
