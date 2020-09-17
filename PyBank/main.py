import os
import csv

bank_csv = os.path.join('Resources', 'budget_data.csv')

with open(bank_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    period = []
    profit_loss = []

    for row in csvreader:

        dates = row[0]
        period.append(dates)
        profit = int(row[1])
        profit_loss.append(profit)
    
       
    change = [profit_loss[i] - profit_loss[i-1] for i in range(len(profit_loss)-1)]
    total_months = len(period)
    netProfit = sum(profit_loss)
    average = round(sum(change) / len(change),2)
    
    maxChange = change.index(max(change))
    minChange = change.index(min(change))
    
    print('Financial Analysis')
    print('-------------------------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${netProfit}')
    print(f'Average Change: ${average}')
    print(f'Greatest Increase in Profits: {period[maxChange]} (${profit_loss[maxChange]})')
    print(f'Greatest Decrease in Profits: {period[minChange]} (${profit_loss[minChange]})')
    print('-------------------------------------------------')

    output_path = os.path.join('analysis','new.csv')

    with open(output_path,'w') as newfile:

        csvwriter = csv.writer(newfile,delimiter=',')

        csvwriter.writerow(['Financial Analysis'])
        csvwriter.writerow(['-------------------------------------------------'])
        csvwriter.writerow([f'Total Months: {total_months}'])
        csvwriter.writerow([f'Total: ${netProfit}'])
        csvwriter.writerow([f'Average Change: ${average}'])
        csvwriter.writerow([f'Greatest Increase in Profits: {period[maxChange]} (${profit_loss[maxChange]})'])
        csvwriter.writerow([f'Greatest Decrease in Profits: {period[minChange]} (${profit_loss[minChange]})'])
        csvwriter.writerow(['-------------------------------------------------'])