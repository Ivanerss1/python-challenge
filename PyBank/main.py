import os
import csv

# Define the file path
script_dir = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(script_dir, "Resources", "budget_data.csv")
output_file = "financial_analysis.txt"

# Variables
total_months = 0
net_total = 0
previous_profit = None
changes = []
dates = []

# Read csv file
with open(csvpath, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Update the total number of months
        total_months += 1

        # Update the net total amount of "Profit/Losses"
        profit = int(row["Profit/Losses"])
        net_total += profit

        # Calculate the monthly change in "Profit/Losses"
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            dates.append(row["Date"])

        previous_profit = profit

# Calculate the average change
average_change = sum(changes) / len(changes)

# Identify the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_decrease = min(changes)
greatest_increase_date = dates[changes.index(greatest_increase)]
greatest_decrease_date = dates[changes.index(greatest_decrease)]

# Prepare the analysis result
analysis = (
    "Financial Analysis\n"
    "-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the results to the terminal
print(analysis)

# Export the results to a text file
with open(output_file, "w") as file:
    file.write(analysis)