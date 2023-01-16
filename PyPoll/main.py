import csv
with open('/Users/castahl/Desktop/UTSA/Bootcamp/Challenges/python challenge /python-challenge/PyPoll/Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  # by doing this we are setting comma as the sign that separates values.
    # to read headers
    header = next(csvreader)

    #variables (so far I know three for sure)
    ballotid=[]
    county=[]
    candidate=[]
