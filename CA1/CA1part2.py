#Assignment 1
#L00158616
#Daniel Gallagher
#Submission Due: 3rd November 

#Part 2:
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
    #adding the random values to the array randomStr
    randomStr = [d1, d2, d3, d4, d5, d6]
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
    #setting CovidId to the type of vaccine e.g AZ or MO
    CovidId = typeOfVaccine
    #for every num in randomStr
    for num in randomStr:
        #Add num to CovidId
        CovidId = CovidId + num
    #Adding checkDigit to covidID   
    CovidId = CovidId + checkDigit   
    return CovidId

#validateCovidId() - will accept a CovidCertID and will determine if it is valid or not.
def validateCovidId(CovidCertId):
    if CovidCertId[:2] == 'AZ':
        return "Your vaccine type is " + CovidCertId[:2] + ": AstraZeneca and your CovidID is valid"
    elif CovidCertId[:2] == 'MO':
        return "Your vaccine type is " + CovidCertId[:2] + ": Moderna and your CovidID is valid" 
    elif CovidCertId[:2] == 'JA':
        return "Your vaccine type is " + CovidCertId[:2] + ": Janssen and your CovidID is valid" 
    elif CovidCertId[:2] == 'PF':
        return "Your vaccine type is " + CovidCertId[:2] + ": Pfizer/BioNTech and your CovidID is valid"
    else:
        return "Error : Invalid Vaccine Type" 

#Write a method that accepts a list as an argument and a vaccination type and
#returns a list of CovidCert IDs of given type
def getListOfCovidIDs(listID, vacType):
    #sets a list called c
    c = []
    #iterates through the list listID
    for vaccID in listID:
        #checks if the vaccID starts with AZ and if the vacType is equal to it
        if vaccID [:2] == "AZ" and vacType == "AZ":
            c.append(vaccID) #adds the vaccID AZ to the list c
        #checks if the vaccID starts with MO and if the vacType is equal to it    
        if vaccID [:2] == "MO" and vacType == "MO":
            c.append(vaccID) #adds the vaccID MO to the list c
        if vaccID [:2] == "JA" and vacType == "JA":
            c.append(vaccID) 
        if vaccID [:2] == "PF" and vacType == "PF":
            c.append(vaccID)  
    return c

#declaring a list and a option choice so the while loop dosent terminate
covidCertIDlist= []
option = ""

#making a loop to add covidIDs to the list covidCertIDlist
while option != "E":
    #Display menu to user and then ask for a option
    print("AZ. - AstraZenca")
    print("MO. - Moderna")
    print("JA. - Janssen")
    print("PF. - Pfizer/BioNTech")
    print("E. Exit")
    #ask the user for an option and store it 
    option = input("Please enter a Choice: ")
    if option == "AZ":
        #generate a covidID AZ and save it to covidCertID 
        covidCertID = generateCovidId(option)
        #add the covidCertID to the list covidCertIDlist
        covidCertIDlist.append(covidCertID)
    if option == "MO":
        #generate a covidID MO and save it to the covidCertID
        covidCertID = generateCovidId(option)
        #add the covidCertID to the list covidCertIDlist
        covidCertIDlist.append(covidCertID)   
    if option == "JA":
        covidCertID= generateCovidId(option)
        covidCertIDlist.append(covidCertID)  
    if option == "PF":
        covidCertID = generateCovidId(option)
        covidCertIDlist.append(covidCertID)  

#removes any of the same covidCertIDs from the list to ensure that the ids are unique
covidCertIDlist2 = list(dict.fromkeys(covidCertIDlist))
print(covidCertIDlist2)

#making a second option for the second while loop that will determine the number of people with a particular vaccine
option2 = ""
#making a loop that will determine the number of people with a particular vaccine
while option2 != "Q":
    #storing a input from the user for the vaccine type
    option2 = input("Please enter a vaccine type [AZ, MO, JA, PF] (press Q to quit): ")
    #if the option is not equal to Q
    if option2 != "Q":
        #get listOfCovidIDs by getting the users vaccine type and using the covidCertIDlist
        ListOfCovidIDs = getListOfCovidIDs(covidCertIDlist, option2)
        print("There is", len(ListOfCovidIDs), "people that has the ", option2, "vaccine type ")
        #print listOFCovidIDs to the user
        print(ListOfCovidIDs)
    else:
        #prints to the user goodbye if they select the option Q
        print("GoodBye")     
        

