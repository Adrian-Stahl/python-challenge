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
    pros = 0
    # variables for 2nd,3rd, 4rd, and 5th task
    alpha = 0
    beta = 0
    gamma = 0
    delta = 0

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
# print(count)  # test and checkpoint
# so we first need to create a list of different candidates: they will have to go through
# candidates and placed them on their own list if they are different.
name.append(candidate[0])

# go through candidate, if different, append to another list called "name"
# -----
for alpha in range(count - 1):
    if candidate[alpha + 1] != candidate[alpha] and candidate[alpha + 1] not in name:
        name.append(candidate[alpha + 1])
amountofCandidates = len(name)

# print test and checkpoint
# print(amountofCandidates) only three candidates in this whole list! good job for today.
# ------
for beta in range(amountofCandidates):
    candidatetotal.append(candidate.count(name[beta]))

# ------
# this is where we obtain the percentage

for gamma in range(amountofCandidates):
    candidatepercent.append(f'{round((candidatetotal[gamma] / count * 100), 3)}%')  # We use an f string because we are
    # creating a statment with different data types.

    # print(candidatepercent)
    # print(name)
    # print(amountofCandidates)
    # print(candidatetotal)

    # let's use pi to display results

for theta in range(amountofCandidates):
    pi.append(f'{name[theta]}: {candidatepercent[theta]}    ({candidatetotal[theta]})')  # this should put everything in
    # order

    # print(pi)
finalTally = '\n'.join(pi)
# print(finalTally)

finalWork = f'\
Election Results\n\
-------------------------\n\
Total Votes: {count}\n\
-------------------------\n\
{finalTally}\n\
-------------------------\n'

print(finalWork)

# pypoll = open("pypoll.txt", 'w')
# pypoll.writelines(finalWork)
# pypoll.close()
