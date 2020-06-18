import csv
import os

#FINDING THE PATH TO THE CSV FILE
path = os.path.abspath("DATA\\REFERENCE.csv")

def getLabel(filestr):

#FINDING THE INDEX
    filestr = filestr.replace("A"," ")             #takes the input and removes the A char
    filestr = filestr.lstrip('0')                  #strips leading zeros
    idx = int(filestr)                             #converts filestr to a usable index and then is stored in idx

#READING THE FILE
    with open(path,'r') as csv_file:                #opens the file
        csv_reader = list(csv.reader(csv_file))     #reads the csv and then puts it in a list
        label = csv_reader[idx][1:]                 #the output is the line from the list indexed by the input
        return(label)


#CODE TO TEST THE FUNCTION
"""test1 = getLabel("A0001")
print(test1)

test2 = getLabel("A0043")
print(test2)"""





