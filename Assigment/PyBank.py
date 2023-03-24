import os
import csv

csvpath = r"Resources\budget_data.csv"

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    csv_header = next(csvreader)
    
    
    months = []
    profit_loss_changes = []

    count_months = 0
    net_profit_loss = 0
    previous_month_profit_loss = 0
    current_month_profit_loss = 0
    profit_loss_change = 0
             
    
    for row in csvreader:

   
        count_months += 1

        
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            
            months.append(row[0])
            
            profit_loss_changes.append(profit_loss_change)
            
            previous_month_profit_loss = current_month_profit_loss

    
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

summaryTable = f"""Financial Analysis
-------------------------
Total Months:  {count_months}
Total:  ${net_profit_loss}
Average Change:  ${average_profit_loss}
Greatest Increase in Profits:  {best_month} (${highest_change})
Greatest Decrease in Losses:  {worst_month} (${lowest_change})"""

print(summaryTable)
#write summary string
with open("budget_data.txt", "w") as file1:
    file1.write(summaryTable)