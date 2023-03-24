# import the necessary libraries
import csv
import os

# set the file path for the data
data_path = os.path.join("Resources", "budget_data.csv")

# open the file and create a csv reader object
with open(data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip the header row

    # initialize variables
    total_months = 0
    total_profit_loss = 0
    profit_loss_changes = []
    dates = []

    # loop through each row of the data
    for row in csvreader:
        # increment the total number of months and the total profit/loss
        total_months += 1
        total_profit_loss += int(row[1])
        dates.append(row[0])

        # calculate the changes in profit/loss and add them to a list
        if total_months > 1:
            profit_loss_changes.append(int(row[1]) - prev_profit_loss)
        prev_profit_loss = int(row[1])

    # calculate the average change in profit/loss and the greatest increase and decrease
    average_change = round(sum(profit_loss_changes) / len(profit_loss_changes), 2)
    greatest_increase = max(profit_loss_changes)
    greatest_decrease = min(profit_loss_changes)
    increase_date = dates[profit_loss_changes.index(greatest_increase) + 1]
    decrease_date = dates[profit_loss_changes.index(greatest_decrease) + 1]

    # format the output
    output_lines = [
        "Financial Analysis",
        "---------------------------",
        f"Total Months: {total_months}",
        f"Total: ${total_profit_loss}",
        f"Average Change: ${average_change}",
        f"Greatest Increase in Profits: {increase_date} (${greatest_increase})",
        f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease})"
    ]

    # print the output to the terminal
    for line in output_lines:
        print(line)

    # export the output to a text file
    with open("output.txt", "w") as txtfile:
        for line in output_lines:
            txtfile.write(line + "\n")
