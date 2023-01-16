import csv

with open('/Users/castahl/Desktop/UTSA/Bootcamp/Challenges/python challenge/python-challenge/PyPoll/Resources/election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  # by doing this we are setting comma as the sign that separates
    # values.
    # to read headers
    header = next(csvreader)

    # variables
    ballotid = []
    county = []
    candidate = []
    name = []
    candidatetotal = []
    candidatepercent = []

    # complete variables according to tasks
    count = 0
    cons = 0
    pros = 0

    # this is how we let python know in which column are the date and earnings
    for row in csvreader:
        id = row[0]
        where = row[1]
        who = row[2]
        # now append
        ballotid.append(id)
        county.append(where)
        candidate.append(who)

# first task is total number of votes cast
count = len(ballotid)
print(count)
