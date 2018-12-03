#Make sure there are no extra parts in the list
#Make sure there are no companies that don't make any irrelevant parts
#confirm if there are companies that need to be in there
#does not account for ties in part price


import csv

#Takes a CSV file of the following form 'company name','part #',price (float)
def readCSV(fileName):
	returnList =[]
	with open(fileName) as f_obj:
		reader = csv.reader(f_obj, delimiter=',')
		for row in reader:
			currentRow=row
			currentRow[2]=float(currentRow[2])
			returnList.append(row)
	return returnList

def column(array,column):
	return [row[column] for row in array]
	
def uniqueValues(array):
	return len(set(array))
	
def makeCompanyList(originalData,companies):
	companyList=[]
	for i in range(0,len(companies)):
		partsList=[]
		for j in range(0,len(originalData)):
			if(originalData[j][0]==companies[i]):
				partsList.append([originalData[j][1],originalData[j][2]])
		companyList.append(partsList)
	return companyList


#Creates an array of the parts for each company at a given index
def createPartsList(parts,index):
	companyParts=parts[index]
	output=[]
	for i in range(0,len(companyParts)):
		output.append(companyParts[i][0])
	return output

def ifPartMadeByCompany(parts,part):
	returnValue=False
	for i in range(0,len(parts)):
		if(part==parts[i]):
			returnValue=True
	return returnValue

#parts: main list with company as key and parts price pairs as list
#selectCompanies: The indexes of companies chosen (will run through every combination)
#partsList:list of parts needed
def findMinimumPartPrice(parts,selectCompanies,partsList):
	minimumPartsCompanyList=[]
	minimumPartsPriceList=[]
	#populate minimumPartsList
	for i in range(0,len(partsList)):
		minimumPartsCompanyList.append(-1)
		minimumPartsPriceList.append(-1)
	#for all the needed parts
	for i in range(0,len(partsList)):
		#for each of the selectedCompanies
		for j in range(0,len(selectCompanies)):
			companyParts=createPartsList(parts,selectCompanies[j])
			#see if the company makes the part, and if it's the first item
			if(ifPartMadeByCompany(companyParts,partsList[i])):
				partPrice=parts[selectCompanies[j]][companyParts.index(partsList[i])][1]
				#if the price is less than the current item
				if(partPrice<minimumPartsPriceList[i] or minimumPartsPriceList[i]==-1):
					#if it makes the part then add it to the list
					minimumPartsCompanyList[i]=selectCompanies[j]
					minimumPartsPriceList[i]=partPrice
	return [minimumPartsCompanyList,minimumPartsPriceList]


#parts: main list with company as key and parts price pairs as list
#companies: Only list of company names
#setNumber: number of companies to be chosen from list to minimize
#partsList:list of parts needed
def goThroughCombinations(parts,companies,setNumber,partsList):
	answers=[]
	minPrice=-1
	for i in range(0,len(companies)-setNumber+1):
		currentList=[]
		for j in range(0,setNumber-1):
			currentList.append(i+j)
		for j in range(setNumber-1+i,len(companies)):
			currentList.append(j)
			#Run main program with list of companies to include in currentList
			tempAnswer=findMinimumPartPrice(parts,currentList,partsList)
			price=0;
			solutionPossible=True #assume that you can find a solution
			for k in range(0,len(tempAnswer[1])):
				if(tempAnswer[1][k]==-1):
					solutionPossible=False #if there's a -1 it wasn't initialized and there were no possible solutions
				price=price+tempAnswer[1][k]
			if(solutionPossible and (minPrice>price or minPrice==-1)):
				answers=tempAnswer
				minPrice=price
			print currentList
			currentList.pop()
	return answers


#data=[['Company A',"Part 3",1],
#['Company B',"Part 1",1],['Company B',"Part 2",1],['Company B',"Part 3",.1],
#['Company C',"Part 1",1],['Company C',"Part 2",.1],['Company C',"Part 3",1],['Company A',"Part 2",1],
#['Company D',"Part 1",1],['Company A',"Part 1",.5],['Company D',"Part 2",.2],['Company D',"Part 3",.2]]
data=readCSV('test1.csv')

companyList=list(set(column(data,0))) #List of all company names
partsList=list(set(column(data,1))) #List of all parts needed
partsByCompany=makeCompanyList(data,companyList)
numCompanies=uniqueValues(column(data,0)) #total number of companies
numParts=uniqueValues(column(data,1)) #total number of parts
selectedCompanies=6
#print partsByCompany
#Run the main part of the program
answers=goThroughCombinations(partsByCompany,companyList,selectedCompanies,partsList)

#make the list of company names
companyNames=[]
for i in range(0,len(answers[0])):
	companyNames.append(companyList[answers[0][i]])
	
#print out answers
print companyNames
print partsList
print answers[1]
bestPrice=0
for i in range(0,len(answers[1])):
	bestPrice=bestPrice+answers[1][i]
print bestPrice

