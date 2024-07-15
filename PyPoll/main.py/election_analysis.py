import csv
import os

# Define the file path
csvpath = '/Users/ivaniac/Documents/Starter_Code/PyPoll/Resources/election_data.csv'
output_file = 'election_results.txt'

# Variables
total_votes = 0
candidate_votes = {}

# Read csv
with open(csvpath, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # total number of votes
        total_votes += 1

        # candidate's vote count
        candidate = row["Candidate"]
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1

# percentage of votes 
candidate_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidate_votes.items()}

#winner based on vote
winner = max(candidate_votes, key=candidate_votes.get)

# analysis result
analysis = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, votes in candidate_votes.items():
    percentage = candidate_percentages[candidate]
    analysis += f"{candidate}: {percentage:.3f}% ({votes})\n"

analysis += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print 
print(analysis)

# Export
with open(output_file, "w") as file:
    file.write(analysis)