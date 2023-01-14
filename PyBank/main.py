# we need to import the csv file from which we are going to draw data from "budget_data.csv"


import csv

with open('budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',') #by doing this we are setting comma as the sign that separates values.

#Since the dataset has a couple of columns named "Date" and "Profit/Losses" we need it to read these columns by creating lists.
#lets create lists as we need to keep order of these elements.
    date=[] # for the date column
    profitloss=[] # for the Profit/Losses column

#complete VARIABLES according to tasks:
    months=0
    average=0
    total=0
    month=0
    differentiaa=0
    differentiab=0
    diferenciaa=0
    diferenciab=0
    x=0
    y=0
    total=0

    month=0

#The total number of months included in the dataset
    month = len(months)


