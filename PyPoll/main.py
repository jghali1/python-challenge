#pypoll

# Interract with filesystems
import os
import csv
from pathlib import Path

# Locate the file
csvpath = os.path.join("Resources","election_data.csv")

# Create lists for data storage
total_votes =0
diana =0
charles =0
raymon =0

# Open the csv
with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through csv 
    for row in csvreader:

        total_votes +=1
        if row[2] =="Diana DeGette":
            diana +=1
        elif row[2] =="Charles Casper Stockham":
            charles+=1
        elif row[2] =="Raymon Anthony Doane":
            raymon+=1

candidates=["Diana DeGette","Charles Casper Stockham","Raymon Anthony Doane"]   
votes=[diana,charles,raymon]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

diana_percent = (diana/total_votes) *100
charles_percent = (charles/total_votes) * 100
raymon_percent = (raymon/total_votes)* 100


print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Diana DeGette: {diana_percent:.3f}% ({diana})")
print(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles})")
print(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

#print
output_file = os.path.join("analysis","output.csv")

with open(output_file,"w") as file:

    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write(f"----------------------------\n")
    file.write(f"Diana DeGette: {diana_percent:.3f}% ({diana})\n")
    file.write(f"Charles Casper Stockham: {charles_percent:.3f}% ({charles})\n")
    file.write(f"Raymon Anthony Doane: {raymon_percent:.3f}% ({raymon})\n")
    file.write(f"----------------------------\n")
    file.write(f"Winner: {key}\n")
    file.write(f"----------------------------\n")  