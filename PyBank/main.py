## Importing the OS and csv
import os
import csv

## Providing the path for the csv file to use
csvpath = os.path.join('Resources', 'budget_data.csv')

## Establishing variables
unique_months = set()

profit_losses_total = 0
profit_loss = []

greatest_increase = 0
increase_month = None
previous_month_value = None

greatest_decrease = 0
decrease_month = None
previous_month_value2 = None

## Reading the csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=",")

## Next - Skipping the header
    next(budget_csv)

## Total number of months included in dataset 
    for row in budget_csv:
        month = tuple(row[0].split('-'))
        unique_months.add(month)

    total_months = len(unique_months)

    print(f"Total Months: {total_months}")

## Net total amount of "Profit/Losses" over the entire period
    csvfile.seek(0)

    next(budget_csv)

    for row in budget_csv:
        profit_losses_total += int(row[1])

    print(f"Total: ${profit_losses_total}")

## Changes in "Profit/Losses" over the entire period and then the average of those changes
    csvfile.seek(0)

    next(budget_csv)

    row = next(budget_csv)
    previous_profit_loss = int(row[1])
    profit_changes = []

    for row in budget_csv:
        current_profit_loss = int(row[1])
        profit_change = current_profit_loss - previous_profit_loss
        profit_changes.append(profit_change)
        previous_profit_loss = current_profit_loss

    average_change = sum(profit_changes) / len(profit_changes) if len(profit_changes) > 0 else 0

    print(f"Average Change: ${average_change:.2f}")

## Greatest increase in profits (date and amount) over the entire period
    csvfile.seek(0)

    next(budget_csv)

    for row in budget_csv:
        current_month_value = int(row[1])

        if previous_month_value is not None:
            increase = current_month_value - previous_month_value
            if increase > greatest_increase:
                greatest_increase = increase
                increase_month = row[0]

        previous_month_value = current_month_value

    if increase_month is not None:
        print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")  
 
## Greatest decrease in profits (date and amount) over the entire period
    csvfile.seek(0)

    next(budget_csv)

    for row in budget_csv:
        current_month_value2 = int(row[1])

        if previous_month_value2 is not None:
            decrease = current_month_value2 - previous_month_value2
            if decrease < greatest_decrease:
                greatest_decrease = decrease
                decrease_month = row[0]

        previous_month_value2 = current_month_value2

    if decrease_month is not None:
        print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")  

## Export text file
    output_path = os.path.join("analysis", "analysis.txt")

    with open(output_path, "w") as textfile:

        textfile.write(f"Total Months: {total_months}\n")
        textfile.write(f"Total: ${profit_losses_total}\n")
        textfile.write(f"Average Change: ${average_change:.2f}\n")
        textfile.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
        textfile.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")
