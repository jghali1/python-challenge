# python-challenge

# Interract with filesystems
import os
import csv
from pathlib import Path

# Locate the file
csvpath = os.path.join("Resources","budget_data.csv")

# Create lists for data storage
months =[]
net_total=[]
changes=[]
greatest_increase=[]
greatest_decrease=[]

# Open the csv
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header=next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through csv searching for months and values
    for row in csvreader:
        print(row)
        months.append(row[0])
        net_total.append(int(row[1]))

    for i in range(len(net_total)-1):
        changes.append(net_total[i+1]-net_total[i])

greatest_increase = max(changes)
greatest_decrease = min(changes)

max_increase_month = changes.index(max(changes)) + 1
max_decrease_month = changes.index(min(changes)) + 1 

# Financial analysis summary calculation
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Change: {round(sum(changes)/len(changes),2)}")
print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(greatest_increase))})")
print(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(greatest_decrease))})")

# Set variable for output file

output_file = os.path.join("analysis","output.csv")

with open(output_file,"w") as file:

    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(months)}\n")
    file.write(f"Total: ${sum(net_total)}\n")
    file.write(f"Average Change: {round(sum(changes)/len(changes),2)}\n")
    file.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(greatest_increase))})\n")
    file.write(f"Greatest Decrease in Profits: {months[max_decrease_month]} (${(str(greatest_decrease))})\n")
 
