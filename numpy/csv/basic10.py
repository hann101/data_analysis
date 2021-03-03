# basic10.py
import glob, csv, sys, os

# File Name, Total sales, Average sales
# A.csv, 2000, 667.666
# B.csv, 2000, 667.666
# C.csv, 2000, 667.666

dir = os.path.dirname(os.path.realpath(__file__))

input_path = dir + '/'
output_file = dir + '/output/output11.csv'

output_header_list = ['File Name', 'Total sales', 'Average sales']
csv_result_file = open(output_file, 'a', newline='')
filewriter = csv.writer(csv_result_file)
filewriter.writerow(output_header_list)

quarter_total = 0.0
quarter_cnt = 0.0
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
    with open(input_file, 'r', newline='') as csv_in_file:
        filereader = csv.reader(csv_in_file)
        output_list = []
        output_list.append(os.path.basename(input_file))
        header = next(filereader)
        total_sales = 0.0
        sales_cnt = 0.0
        for row in filereader:
            sale_amount = row[3] # "$1,350.00"
            total_sales += float(str(sale_amount).strip('$').replace(',', ''))
            sales_cnt += 1.0
        average_sales = '{0:.2f}'.format(total_sales / sales_cnt)
        output_list.append(total_sales)
        output_list.append(average_sales)
        filewriter.writerow(output_list)

        quarter_total += total_sales
        quarter_cnt += sales_cnt

summary_list = ['Summary of the first qurater']
summary_list.append(quarter_total)
print("{}/{}".format(quarter_total, quarter_cnt))
summary_list.append('{0:.2f}'.format(quarter_total / quarter_cnt))
filewriter.writerow(summary_list)

csv_result_file.close()
print("Done.")
            