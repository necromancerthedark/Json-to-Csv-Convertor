import json
import csv
import io

filepath = input("Enter Path to your Json File: ")
csv_filepath = input("Enter Name of your Csv File:")
csv_filepath_format = csv_filepath + '.csv'

json_file = io.open(filepath, 'r+', encoding="utf-8")
csv_file = io.open(csv_filepath_format, 'w+', encoding="utf-8")

json_parsed = json.loads(json_file.read())
csvwriter = csv.writer(csv_file)

for emp in json_parsed:
    csvwriter.writerow(emp.values())

csv_file.close()
