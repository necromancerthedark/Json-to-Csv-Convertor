import json
import csv
import io

json_file = io.open('quotes.json', 'r+', encoding="utf-8")
csv_file = io.open('quotes.csv', 'w+', encoding="utf-8")

json_parsed = json.loads(json_file.read())
csvwriter = csv.writer(csv_file)

print(json_parsed[0]['text'])

for emp in json_parsed:
    csvwriter.writerow(emp.values())

csv_file.close()
