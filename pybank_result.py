import os
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")
with open("budget_data.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)   
for row in csv_reader:
    months = []
    profit_losses = []
count = 0
months_total += 1
net_losses = 0
change = 0
previous_loss = 0
profit_loss = int(row[1])
net_losses += profit_loss
if (months == 1):   
    previous_loss = profit_loss
continue
next
else
change = profit_loss - previous_loss
months.append(row[0])
change.append(profit_losses)
previous_loss = profit_loss
sum_profit_loss = sum(changes)
average_loss = round(sum_profit_loss/(months - 1), 2)
highest_change = max(changes)
lowest_change = min(changes)   
highest_month = changes.index(highest_change)
lowest_month = changes.index(lowest_change)
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {months}")
print(f"Total:  ${net_loss}")
print(f"Average Change:  ${average_loss}")
print(f"Greatest Increase in Profits:  {highest_month} (${highest_change})")
print(f"Greatest Decrease in Profits:  {lowest_month} (${lowest_change})")
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as text_file:
data = file.read().replace('\n', '')
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {months}\n")
    outfile.write(f"Total:  ${net_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {highest_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Profits:  {lowest_month} (${lowest_change})\n")