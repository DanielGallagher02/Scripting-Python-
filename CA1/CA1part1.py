#Assignment 1
#L00158616
#Daniel Gallagher
#Submission Due: 3rd November 

#Part 1:
import random

#getRandomStr() - generates and returns a string of 6 random digits(0 to 9).
def getRandomStr():
    #getting a random number from 0 to 9, making it a string and calling it d1
    d1 = str(random.randint(0, 9)) 
    #getting a random number from 0 to 9, making it a string and calling it d2
    d2 = str(random.randint(0, 9))
    d3 = str(random.randint(0, 9))
    d4 = str(random.randint(0, 9))
    d5 = str(random.randint(0, 9))
    d6 = str(random.randint(0, 9))
    #adding the random values to an array called randomStr
    randomStr = [d1, d2, d3, d4, d5, d6]
    #returning randomStr
    return randomStr
    
#getCalcCheckDigit() - will compute and return the check digit for a random
#sequence passed as an argument.
def calcCheckDigit(ListOfNumbers):
    #gets the first number in a list, making it an int and calling it d1
    d1 = int(ListOfNumbers[0])
    #gets the second number in a list, making it an int and calling it d2
    d2 = int(ListOfNumbers[1])
    d3 = int(ListOfNumbers[2])
    d4 = int(ListOfNumbers[3])
    d5 = int(ListOfNumbers[4])
    d6 = int(ListOfNumbers[5])
    totalValue = (d6*1) + (d5*2) + (d4*3) + (d3*4) + (d2*5) + (d1*6)
    checkDigit = str(totalValue)
    return checkDigit[-1]

#generateCovidId() - will generate a random CovidCert id number of the form CCxxxxxxY
#where CC is one of the allowed vaccine values, x is a random digit and Y is the check
#digit. The type of vaccine should be passed as an argument.
def generateCovidId(typeOfVaccine):
    #get 6 random digits for the covidId
    randomStr = getRandomStr()
    #get the check digit from the randomStr
    checkDigit = calcCheckDigit(randomStr)
    #CovidId is equal to the type of vaccine e.g AZ or MO
    CovidId = typeOfVaccine
    #for every num in randomStr
    for num in randomStr:
        #Add num to CovidId
        CovidId = CovidId + num
    #Adding checkDigit to covidID    
    CovidId = CovidId + checkDigit   
    #returning CovidId
    return CovidId

#validateCovidId() - will accept a CovidCertID and will determine if it is valid or not.
def validateCovidId(CovidCertId):
    #checks if CovidCertId first 2 letters is AZ
    if CovidCertId[:2] == 'AZ':
        #returns if true
        return "Your vaccine type is " + CovidCertId[:2] + ": AstraZeneca and your CovidID is valid"
    #checks if CovidCertIds first 2 letters are MO     
    elif CovidCertId[:2] == 'MO':
        #returns if true
        return "Your vaccine type is " + CovidCertId[:2] + ": Moderna and your CovidID is valid" 
    elif CovidCertId[:2] == 'JA':
        return "Your vaccine type is " + CovidCertId[:2] + ": Janssen and your CovidID is valid" 
    elif CovidCertId[:2] == 'PF':
        return "Your vaccine type is " + CovidCertId[:2] + ": Pfizer/BioNTech and your CovidID is valid"
    else:
        return "Error : Invalid Vaccine Type" 



#Testing the getRandomStr() method 
randomStr1 = getRandomStr()
print(randomStr1)
print()

#Testing the calcCheckDigit(listOfNumbers) method
CheckDigit1 = calcCheckDigit(randomStr1) 
print(CheckDigit1)
print()

#Testing the generateCovidId(typeOfVaccine) method
CovidId1 = generateCovidId("AZ") #generate a covidId of AZ
CovidId2 = generateCovidId("MO")
CovidId3 = generateCovidId("JA")
CovidId4 = generateCovidId("PF")
print(CovidId1) #print covidId1 which prints a AZ covidId e.g AZ5479834
print(CovidId2)
print(CovidId3)
print(CovidId4)
print()

CovidId5 = generateCovidId("AA") # generate a invalid covidId
#Testing validateCovId(CovidCertId) method
vCovidId1 = validateCovidId(CovidId1) #valid covid id
print(vCovidId1)
print()

vCovidId2 = validateCovidId(CovidId5) #invalid covid id 
print(vCovidId2)
print()





         






































