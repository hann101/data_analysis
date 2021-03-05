import pandas as pd
import os
import csv
import glob
import xlrd
from xlrd import open_workbook

_dir = os.path.dirname(os.path.realpath(__file__))

item_numbers_file = _dir +'/item_numbers_to_find.csv'
item_numbers_file2 = _dir+'/historical_files'
output_file = _dir+'/output/output.csv'
item_numbers_to_find = []
with open(item_numbers_file, 'r', newline='') as item_numbers_csv_file:
    filereader = csv.reader(item_numbers_csv_file)
    for row in filereader:
        item_numbers_to_find.append(row[0])

file_counter=0
for input_file in glob.glob(os.path.join(item_numbers_file2, '*.*')):
    file_counter += 1
    if input_file.split('.')[1] == 'csv':
        with open(input_file, 'r', newline='') as csv_in_file:
            with open(output_file , 'a',newline='') as csv_out_file:
                filereader = csv.reader(csv_in_file)
                filewriter = csv.writer(csv_out_file)
                header = next(filereader)
                for row in filereader:
                    row_of_output = []
                    for column in range(len(header)):
                        count_of_item_numbers=0
                        line_counter=0
                        
                        if column < 3:
                            cell_value = str(row[column]).strip()
                            row_of_output.append(cell_value)
                        elif column == 3:
                            cell_value = str(row[column]).lstrip('$').replace(',','').split('.')[0].strip()
                            row_of_output.append(cell_value)
                        else:
                            cell_value = str(row[column]).strip()
                            row_of_output.append(cell_value)
                    
                    row_of_output.append(os.path.basename(input_file))
                            
                    if row[0] in item_numbers_to_find:
                        filewriter.writerow(row_of_output)
                        count_of_item_numbers += 1
                    line_counter += 1

        