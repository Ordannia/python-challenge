# Import needed things
import os
import csv
from collections import Counter

    # Used my brain
    # And Xpert Learning Assistant for Counter

## Print title
## Should look like: Election Results
print("\nElection Results")

## Print separation line
## Should look like: -----------------------------------------
print(f"\n-------------------------\n")

## Providing the path for the csv file to use
csvpath = os.path.join('Resources', 'election_data.csv')
    ## Used code from PyBank

# Establishing variables
total_votes = set()

candidate_column = 2
candidate = []

## Reading the csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    election_csv = csv.reader(csvfile, delimiter=",")

#Skipping the header
    next(election_csv)

## Total Votes
## Should look like: Total Votes: 369711
    for row in election_csv:
        votes = tuple(row[0].split('-'))
        total_votes.add(votes)

    total = len(total_votes)

    print(f"Total Votes: {total}\n\n-------------------------\n")

## Print separation line
## Should look like: ------------------------------------------


## Complete list of candidates who received votes
    ## Percentage of votes received per candidate
    ## Total number of votes per candidate
## Should look like:
## Charles Casper Stockham: 23.049% (85213)
##
## Diana Degette: 73.812% (272892)
##
## Raymon Anthony Doane: 3.139% (11606)
    csvfile.seek(0)

    next(election_csv)

    for row in election_csv:
        if len(row) > candidate_column:
            name = row[candidate_column].strip()
            candidate.append(name)

    candidate_counts = Counter(candidate)

    for candidate, count in candidate_counts.items():
        candidate_percentage = round((count / total) * 100, 3)
        print(f"{candidate}: {candidate_percentage}% {count}")
        print()    
    # Used Xpert Learning Assistant
## Print separation line
## Should look like: ------------------------------------------
    print(f"-------------------------\n")

## Winner based on popular vote
## Should look like: Winner: Diana Degette
    winner = max(candidate_counts, key=candidate_counts.get)
    print(f"Winner: {winner}")

## Print separation line
## Should look like: ------------------------------------------
    print(f"\n-------------------------")

## Export to txt
    output_path = os.path.join("analysis", "analysis.txt")

    with open(output_path, "w") as textfile:

        textfile.write("\nElection Results\n")
        textfile.write(f"\n-------------------------\n\n")
        textfile.write(f"Total Votes: {total}\n\n-------------------------\n\n")

        for candidate, count in candidate_counts.items():
            candidate_percentage = round((count / total) * 100, 3)
            textfile.write(f"{candidate}: {candidate_percentage}% {count}\n\n")
        
        textfile.write(f"-------------------------\n")
        textfile.write(f"\nWinner: {winner}\n")
        textfile.write(f"\n-------------------------")