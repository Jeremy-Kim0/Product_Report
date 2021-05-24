import csv

def createInput():
    #Creates example ProductMaster.csv
    with open('ProductMaster.csv', 'w', newline='') as product:
        csvwriter1 = csv.writer(product)
        csvwriter1.writerow(['1', 'Minor Widget', '0.25', '250'])
        csvwriter1.writerow(['2', 'Critical Widget', '5.00', '10'])
        csvwriter1.writerow(['3', 'Complete System (Basic)', '500', '1'])
        csvwriter1.writerow(['4', 'Complete System (Deluxe)', '625', '1'])

    #Creates example Sales.csv
    with open('Sales.csv', 'w', newline='') as sale:
        csvwriter2 = csv.writer(sale)
        csvwriter2.writerow(['1', '1', '2', '10'])
        csvwriter2.writerow(['2', '1', '1', '1'])
        csvwriter2.writerow(['3', '2', '1', '5'])
        csvwriter2.writerow(['4', '3', '4', '1'])
        csvwriter2.writerow(['5', '3', '5', '2'])
