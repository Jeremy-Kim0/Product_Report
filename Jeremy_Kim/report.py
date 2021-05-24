import sys
import createCSV
import csv
import operator
import os.path

#Error checking for correct number of user inputted arguments
if len(sys.argv) != 4:
    print("Incorrect number of arguments. Expected four input arguments")
    quit()

#Initalizing Variables
input1 = sys.argv[1]
input2 = sys.argv[2]
input3 = sys.argv[3]
listRev = []
indexRev = []
num=0;

if not os.path.isfile(input1) and not os.path.isfile(input2):
    # Function to create sample and ProductMaster.csv Sales.csv if not already provided
    createCSV.createInput()

#Opens the input files to read
with open(input1, 'r', newline='') as product:
    product_Reader = csv.reader(product)

    with open(input2, 'r',newline='') as sales:
        sales_Reader = csv.reader(sales)

        with open("temp.csv", 'w', newline='') as output:
            output_Writer = csv.writer(output, delimiter=',')
            # Populates a temp file with name, GrossRevenue, TotalUnits (non sorted)
            for line in sales_Reader: #for loop goes through each line in the Sales.csv file
                product.seek(0)
                for lineP in product_Reader: #for loop finds the desired product through productID
                    if int(lineP[0]) == int(line[1]):
                        price = lineP[2]
                        lotSize = lineP[3]
                        name = lineP[1]
                        break
                # TotalUnits = Quantity * LotSize
                TotalUnits = float(line[3])*float(lotSize)
                #GrossRevenue = Price * TotalUnits
                GrossRevenue = float(price)*TotalUnits
                rev = int(GrossRevenue)
                listRev.append([num, rev]) #List of index and GrossRevenue
                num += 1
                output_Writer.writerow([name, str(GrossRevenue), str(TotalUnits)])

            output.close()

            with open("temp.csv", 'r', newline='') as original:
                csv_Reader = csv.reader(original)
                rows = list(csv_Reader)
                with open(input3, 'w', newline='') as sortedList:
                    output_Writer = csv.writer(sortedList, delimiter=',')
                    counter=0
                    #Sorts the temp file in GrossRevenue descending order
                    indexRev = sorted(listRev, key=operator.itemgetter(1), reverse=True)
                    #Sets header
                    output_Writer.writerow(['Name', 'GrossRevenue', 'TotalUnits'])

                    for x in indexRev:
                        #Finds correct row based on GrossRevenue
                        rowsIndex = int((indexRev[int(counter)])[0])
                        #Writes row to output
                        output_Writer.writerow(rows[rowsIndex])
                        counter += 1







