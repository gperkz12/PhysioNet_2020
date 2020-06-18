import csv
import os

path = os.path.abspath("DATA\\REFERENCE.csv")

def get_label(filestr):

    filestr = filestr.replace("A"," ")
    filestr = filestr.lstrip('0')
    idx = int(filestr)


    with open(path,'r') as csv_file:
        csv_reader = list(csv.reader(csv_file))

        print(csv_reader[idx][1:])



get_label("A1002")