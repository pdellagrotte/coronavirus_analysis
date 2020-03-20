import os
import csv
from csv import reader
from csv import writer

output_folder = 'processed/'
ROOT_FOLDER = 'C:/Users/paul.dellagrotte/Documents/Projects/Python/coronovirus_analysis/data/jh_daily_cases/'


def add_column_in_csv(input_file, output_file, cols):
    with open(input_file) as f:
        with open(output_file, 'w') as w:
            reader = csv.reader(f)
            writer = csv.writer(w, lineterminator="\n")
            all = []
            for row in reader:
                all.append(row + cols)
            writer.writerows(all)


def file_column_length_handler(filename):  # returns number of columns in .CSV file
    d = ','
    f = open(filename, 'r')
    reader = csv.reader(f, delimiter=d)
    ncol = len(next(reader))  # Read first line and count columns
    return ncol


for file in os.listdir(ROOT_FOLDER):
    input_file = ROOT_FOLDER + file
    output_file = ROOT_FOLDER + output_folder + file
    if file_column_length_handler(ROOT_FOLDER + file) == 6:
        add_column_in_csv(input_file, output_file, ["Latitude", "Longitude", file[0:10]])
    else:
        add_column_in_csv(input_file, output_file, [file[0:10]])
