# we need to import the csv file from which we are going to draw data from "budget_data.csv"


import csv

with open('/Users/castahl/Desktop/UTSA/Bootcamp/Challenges/python challenge /python-challenge/PyBank/Resources/budget_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  # by doing this we are setting comma as the sign that separates values.
    # to read headers
    header = next(csvreader)

    # Since the dataset has a couple of columns named "Date" and "Profit/Losses" we need it to read these columns by creating lists.
    # lets create lists as we need to keep order of these elements.
    date = []  # for the date column
    profitloss = []  # for the Profit/Losses column

    # complete VARIABLES according to tasks:
    months = 0
    average = 0
    total = 0
    ma = 0
    differentiaa = 0
    differentiab = 0
    diferenciaa = 0
    diferenciab = 0
    x = 0
    y = 0
    total = 0

    mb = 0

    # this is how we let python know in which column are the date and earnings
    for row in csvreader:
        monthyear = row[0]
        earnings = row[1]
        date.append(monthyear)
        profitloss.append(earnings)
        # The total number of months included in the dataset
    ma = len(date)


    for x in range (ma-1):
        average = average + (float(profitloss[x+1]) - float(profitloss[x]))
        mb = (float(profitloss[x+1]) - float(profitloss[x]))

        if mb < differentiab:
            differentiab = mb
            diferenciab = x
        else:
            differentiab = differentiab

        if mb > differentiaa:
            differentiaa = mb
            diferenciaa = x
        else:
            differentiaa = differentiaa

    for y in range (ma):
        total = total + int(profitloss[y])
finalWork=f'\
    Financial Analysis\n\
    ----------------------------\n\
    Total Months:{ma}\n\
    Total:${total}\n\
    Average Change: $ {round(average/(ma - 1),2)}\n\
    Greatest Increase in Profits:{date[diferenciaa+1]} ${int(differentiaa)}\n\
    Greatest Decrease in Profits: {date[diferenciab + 1]} ${int(differentiab)}\n'
print(finalWork)

pybank = open("pybank.txt", 'w')
pybank.writelines(finalWork)
pybank.close()
