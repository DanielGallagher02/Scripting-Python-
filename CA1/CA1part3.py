#Assignment 1
#L00158616
#Daniel Gallagher
#Submission Due: 3rd November 

#Part 3:
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
    d1 = int(ListOfNumbers[0])
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
    #getting the 6 random digits for the covidId
    randomStr = getRandomStr()
    #getting the check digit from the randomStr
    checkDigit = calcCheckDigit(randomStr)
    #CovidId is equal to the type of vaccine e.g AZ or MO
    CovidId = typeOfVaccine
    #for every num in randomStrp
    for num in randomStr:
        #Add num to CovidId
        CovidId = CovidId + num
    #Adding the checkdigit to the CovidId    
    CovidId = CovidId + checkDigit   
    #return the CovidId
    return CovidId 

#validateCovidId() - will accept a CovidCertID and will determine if it is valid or not.
def validateCovidId(CovidCertId):
    if CovidCertId[:2] == 'AZ':     #if CovidCertId first 2 letters is equal to AZ
        return "It is Valid"        #return string "It is Valid"
    elif CovidCertId[:2] == 'MO':   #if CovidCertId first 2 letters is equal to MO
        return "It is Valid"        #return string "It is Valid" 
    elif CovidCertId[:2] == 'JA':
        return "It is Valid" 
    elif CovidCertId[:2] == 'PF':
        return "It is Valid"
    else:                                       #if CovidCertId is not equal to the ifs and elifs above like e.g AZ and MO
        return "Error : Invalid Vaccine Type"   #return string Error : Invalid Vaccine Type

#decalring a list called covidCertIDlists and adding some random CovidCert IDs
covidCertIDlist = ["AZ7876984", "AZ3979202", "MO4972718", "MO4919486", "JA9234348", "PF7991584"]
covidCertID = ""
#show the list to the user
print(covidCertIDlist) 
while covidCertID != "Q":
    #use the covidCertID variable to store a CovidCertID entered by the user
    covidCertID = input("Please enter your CovidCert ID to book a ticket (press Q to quit): ")
    #test to see if the covidCertID is valid
    if covidCertID != "Q":
        if validateCovidId(covidCertID) == "It is Valid":
            #if it is valid print your covidCertID is valid 
            print("Your CovidCertID is valid")
            # test to see if it is already in the list
            # if its in the list give the index or position
            if covidCertID in covidCertIDlist:
                print("Your CovidCertID is already in the list")
                covidIDpos = covidCertIDlist.index(covidCertID)
                print("The position or index of your covidcertID in the list is:" + str(covidIDpos))
            else:
                #If it is not in the list, add it to the list
                print("Your CovidCertID is not in the list")
                #printing a string to show the user that it is adding the CovidCertID to the list
                print("Adding your CovidCertID to the list")
                #adds the covidCertID to the list covidCertIDlist
                covidCertIDlist.append(covidCertID)      
        else:
            #prints the CovidCertID is invalid if the covidCert id entered by the user is invalid
            print("Your CovidCertID is invalid")                 
    else:
        #prints goodbye to the user when the user enters Q
        print("Goodbye") 

#prints the list of CovidCertIDs to the user when they have exited the while loop
print(covidCertIDlist)               







