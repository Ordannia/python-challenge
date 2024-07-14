# Import needed things
import os
import csv
from collections import Counter

## Print title
print("\nElection Results")

## Print separation line
print(f"\n-------------------------\n")

## Providing the path for the csv file to use
csvpath = os.path.join('Resources', 'election_data.csv')

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
    for row in election_csv:
        votes = tuple(row[0].split('-'))
        total_votes.add(votes)

    total = len(total_votes)

    print(f"Total Votes: {total}\n\n-------------------------\n")

## Complete list of candidates who received votes
    ## Percentage of votes received per candidate
    ## Total number of votes per candidate
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

## Print separation line
    print(f"-------------------------\n")

## Winner based on popular vote
    winner = max(candidate_counts, key=candidate_counts.get)
    print(f"Winner: {winner}")

## Print separation line
    print(f"\n-------------------------")

## Export to text
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