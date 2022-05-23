import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')
election_text_path = 'analysis/election_analysis.txt'

total_number_of_votes = 0
candidate_votes = {}



with open(csvpath, encoding= 'utf') as csvfile:
     #Initialising reader to read csvfile                   
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    #Skipping the first row (header)
    header = next(csvreader)

    for row in csvreader:
      total_number_of_votes = total_number_of_votes  + 1
      canddate_name = row[2]

      candidate_votes[canddate_name] = candidate_votes.get(canddate_name, 0) + 1

print("\nElection Results\n")
print("-------------------------")
print(f"Total Number of votes: {total_number_of_votes}")
print("-------------------------")

sum_of_votes = sum([v for k, v in candidate_votes.items()])
winner_value = 0
winner_name = ""
for candidate, votes in candidate_votes.items():
  print(f"{candidate}: ", (votes/sum_of_votes)* 100)
  if votes > winner_value:
    winner_value = votes
    winner_name = candidate
print("-------------------------")
print('Winner: ', winner_name)
print("-------------------------")


with open(election_text_path, 'w') as text:
    text.write("\nElection Results\n")
    text.write("-------------------------\n")
    text.write(f"Total Number of votes: {total_number_of_votes}\n")
    text.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
      percentage = round((votes/sum_of_votes)* 100, 2)
      text.write(f"{candidate}: {percentage}%\n")

    text.write(f'\nWinner: {winner_name}\n')
    text.write("-------------------------\n")

