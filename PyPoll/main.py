import csv

with open(
        '/Users/castahl/Desktop/UTSA/Bootcamp/Challenges/python challenge /python-challenge/PyPoll/Resources /election_data.csv') as csvfile:
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
    # list to display percentage of candidates orderly
    pi = []

    # complete variables according to tasks
    count = 0




    # this is how we let python know in which column are the ids, name, and race
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
# so we first need to create a list of different candidates: they will have to go through
# candidates and placed them on their own list if they are different.
name.append(candidate[0])

# go through candidate, if different, append to another list called "name"

for loopforamount in range(count - 1):
    if candidate[loopforamount + 1] != candidate[loopforamount] and candidate[loopforamount + 1] not in name:
        name.append(candidate[loopforamount + 1])
amountofCandidates = len(name)
#print(name)


#With the amountofCandidates list we obtain total votes
for loopfortotalvotes in range(amountofCandidates):
    candidatetotal.append(candidate.count(name[loopfortotalvotes]))


# this is where we obtain the percentage:
#With the amountofCandidates list we ALSO obtain percentage and append results to list candidatepercent
for loopforpercent in range(amountofCandidates):
    candidatepercent.append(f'{round((candidatetotal[loopforpercent] / count * 100), 3)}%')  # We use an f string because we are
    # creating a statment with different data types.

    # print(candidatepercent)
    # print(name)
    # print(amountofCandidates)
    #print(candidatetotal)

    # let's use pi to create a dictionary so we can format

for loopforformat in range(amountofCandidates):
    pi.append(f'{name[loopforformat]}: {candidatepercent[loopforformat]}    ({candidatetotal[loopforformat]})')  # this should put everything in

#We select \n as separator between our keys from our Dictionary
finalTally = '\n'.join(pi)
#print(finalTally)

finalWork = f'\
Election Results\n\
-------------------------\n\
Total Votes: {count}\n\
-------------------------\n\
{finalTally}\n\
-------------------------\n'
#and we display the results in finalWork
print(finalWork)

pypoll = open("pypoll.txt", 'w')
pypoll.writelines(finalWork)
pypoll.close()
