# import os & csv
import os

import csv



# path for csv file
csvpath = os.path.join("Resources","budget_data.csv")



# create lists
profit = []

monthly_changes = []

date = []



# define variables
count = 0

total_profit = 0

total_change_profits = 0

initial_profit = 0



# open csv file
with open(csvpath, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)



    # loop
    for row in csvreader:    

      # count number of rows in file
      count = count + 1 



      # append date list
      date.append(row[0])



      # append the profit list & sum
      profit.append(row[1])

      total_profit = total_profit + int(row[1])



      # change in months

      final_profit = int(row[1])

      monthly_change_profits = final_profit - initial_profit



      # monthly changes list

      monthly_changes.append(monthly_change_profits)



      total_change_profits = total_change_profits + monthly_change_profits

      initial_profit = final_profit



      # average change in profits

      average_change_profits = (total_change_profits/count)

      

      # max & min change in profits

      greatest_increase_profits = max(monthly_changes)

      greatest_decrease_profits = min(monthly_changes)



      increase_date = date[monthly_changes.index(greatest_increase_profits)]

      decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

      

    print("----------------------------------------------------------")

    print("Financial Analysis")

    print("----------------------------------------------------------")

    print("Total Months: " + str(count))

    print("Total: " + "$" + str(total_profit))

    print("Average Change: " + "$" + str(int(average_change_profits)))

    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")

    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")







   





    

