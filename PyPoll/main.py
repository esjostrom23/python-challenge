# import os & csv 
import os

import csv



# csv path 
csvpath = os.path.join("Resources","election_data.csv")



# lists
count = 0

candidatelist = []

unique_candidate = []

vote_count = []

vote_percent = []



# open csv
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    # loop
    for row in csvreader:

        # votes counter
        count = count + 1

        # candidate list
        candidatelist.append(row[2])

        # variable for candidate names
    for x in set(candidatelist):

        unique_candidate.append(x)

        # variable for count of votes

        y = candidatelist.count(x)

        vote_count.append(y)

        # variable for percent of votes

        z = (y/count)*100

        vote_percent.append(z)

        
    winning_vote_count = max(vote_count)

    winner = unique_candidate[vote_count.index(winning_vote_count)]


print("-------------------------")

print("Election Results")   

print("-------------------------")

print("Total Votes :" + str(count))    

print("-------------------------")

for i in range(len(unique_candidate)):

            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")

print("-------------------------")

print("The winner is: " + winner)

print("-------------------------")