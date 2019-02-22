import os
import csv

#data path
budget_data = os.path.join('..', 'Resources', 'budget_data.csv')
with open(budget_data, newline="") as csvfile:

	b_data = csv.reader(csvfile, delimiter=',')
	month_total = list(b_data)
	row_count = len(month_total)
	print(row_count - 1)



# Define the function and have it accept the 'budgetData' as its sole parameter
#total
with open(budget_data) as f:
	rows = csv.DictReader(f)
	total = (sum(float(r['Profit/Losses']) for r in rows))
	print (total)
#average

	averages = (sum(float(r['total'/ len('Profit/Losses')]) for r in rows))
	print(averages)
	average = total / len('Profit/Losses')
	print(average)
	row
	#averages(budget_data):s
	#return [sum(row)/len(row) for row in budget_data]
