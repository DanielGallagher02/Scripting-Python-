#Written by Daniel Gallagher
#L00158616
#Assignment 2
#Due date: 23rd December

from csv import reader
import random
import datetime

#getWordListFromFile(): will accept a filename and return a list
# or unique words over length 7
def getWordListFromFile(aFilename):
    file = open(aFilename, "r")
    content = file.read()
    #print(content)
    content_list = content.split(",")
    file.close()
    return content_list

#selectRandomKey(): will accept a list and return a random choice
#(random.choice())
def selectRandomKey(aList):
    #key must be selected at random  
    randomchoice = random.choice(aList)
    #must not be longer than 7 characters in length and only contain alphabetic letters
    #The keyword should be appended to a file called Keys.txt with current date stamp
    return randomchoice

#buildEncryptionStr(): accepts a keyword and builds and returns the encodingString
def buildEncryptionStr(aKeyword):
    #remove any duplication letters
    nodupletters = "".join(dict.fromkeys(aKeyword))
    #Add the remaining letters of the alphabet to the end of the keyword in reverse order
    alphabet = "abcdefghijklonmpqrstuvwxyz"
    #Adding the nodupLetters and the alaphabet(reverse order) to encodingString 
    encodingString = nodupletters + alphabet[::-1]
    #Remove any duplication letters again
    encodingString = "".join(dict.fromkeys(encodingString))
   
    #return encodingString    
    return encodingString

#encode(): which accepts the encodingString and the file name and encodes
#the text in the file and writes it to the appropriate file.
def encode(encodingString, aFileName):
    #The text will be encoded using the mappings e.g. a → s, b → c, c → r, … y→b, z→a
    #Using the 'scripting' example
    alphabet = "abcdefghijklonmpqrstuvwxyz"
    encoder = {}
    for a in range(len(alphabet)):
        encoder[alphabet[a]] = encodingString[a]

    return ""

#decode(): which accepts the encodingString and the file name and 
#decodes the text in the file and writes it to the appropriate file.
def decode(encodingString, aFileName):
    return ""


#option for the Menu
option = ""
#making a while loop for the menu
while option != 7:
    #Display the menu to the user 
    print("\n ~~~ MENU ~~~")
    print("1. Display contents of any csv file on screen")
    print("2. Display contents of any text file on screen")
    print("3. Select a key word")
    print("4. Generate an encryption string")
    print("5. Encrypt a file")
    print("6. Decrypt a file")
    print("7. Quit")
    #ask the user for an option and store it
    option = int(input("Please enter a option choice: "))

    if option == 1:
        try:
            #try block
            csvfile = input("Please enter the csv file u want to see the contents of:  ")
            print("\n~ Contents ~")
            #opens the file
            infile = open(csvfile)
            #create a CSV reader using the reader function
            csvReader = reader(infile)
            #read each row
            for row in csvReader:
                #print each row
                print(row)
            #closes the file
            infile.close() 

        except IOError:
            print("ERROR - cannot open the non-existent file for reading") 
        except KeyboardInterrupt:
            print("ERROR - cannot input Control-C or Delete") 
        except IndexError:
            print("ERROR - Sequence index out of range")
        except ZeroDivisionError: 
            print("ERROR - Cannot divide by Zero")        


    if option == 2:
        try:
            #Asks the user for a text file they want to see the conetents of
            textfile = input("Please enter the any text file u want to see the contents of:  ") 
            #opens the text file that the user entered
            infile = open(textfile)
            #reads chars from infile until the end of the file is reached
            #Returns characters as a string
            print("\n~ Contents ~")
            print(infile.read())
            #closes the file
            infile.close

        except IOError:
            print("ERROR - cannot open the non-existent file for reading")    
        except KeyboardInterrupt:
            print("ERROR - cannot input Control-C or Delete")
        except IndexError:
            print("ERROR - Sequence index out of range")   
        except ZeroDivisionError: 
            print("ERROR - Cannot divide by Zero")    


    #Select a Keyword
    if option == 3:
        #The keyword must be selected at random from a text file and must be longer than 7 characters 
        #in length and must only contain alphabetic letters
        try:
            textfile2 = input("Please enter the any text file u want the keyword selected from at random : ") 
            selectRandomKey(textfile2)
            #The keyword should be appended to a file called Keys.txt with current date stamp
            append = open('Keys.txt', 'a')
            today = datetime.datetime.now()
            dateTime = today.strftime("%m/$d/%Y, %H:%M:%S")
            append.write(textfile2, dateTime)
            append.close()

        except IOError:
            print("ERROR - cannot open the non-existent file for reading")
        except KeyboardInterrupt:
            print("ERROR - cannot input Control-C or Delete ")   
        except IndexError:
            print("ERROR - Sequence index out of range") 
        except ZeroDivisionError: 
            print("ERROR - Cannot divide by Zero") 

    #Generate a encryption String
    if option == 4:
        try:
            keywordIn = input("Please enter a keyword that u want to use for the encryption string : ") 
            print(buildEncryptionStr(keywordIn))

        except IOError:
            print("ERROR - cannot open the non-existent file for reading")
        except KeyboardInterrupt:
            print("ERROR - cannot input Control-C or Delete ")   
        except IndexError:
            print("ERROR - Sequence index out of range") 
        except ZeroDivisionError: 
            print("ERROR - Cannot divide by Zero")  

    #Encrypt a file
    if option == 5:
        try:   
            print("Option 5")

        except IOError:
            print("ERROR - cannot open the non-existent file for reading")
        except KeyboardInterrupt:
            print("ERROR - cannot input Control-C or Delete ")   
        except IndexError:
            print("ERROR - Sequence index out of range") 
        except ZeroDivisionError: 
            print("ERROR - Cannot divide by Zero")      

    #Decrypt a file
    if option == 6:
        try:
            print("Option 6") 

        except IOError:
            print("ERROR - cannot open the non-existent file for reading")
        except KeyboardInterrupt:
            print("ERROR - cannot input Control-C or Delete ")   
        except IndexError:
            print("ERROR - Sequence index out of range") 
        except ZeroDivisionError: 
            print("ERROR - Cannot divide by Zero")  

    if option == 7:
        print("Succesfully exited, Goodbye")   

                       





    

    




                   
            