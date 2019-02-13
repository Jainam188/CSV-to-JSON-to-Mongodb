import csv
import json

f = open('filename.csv', 'rU')

reader = csv.DictReader(f, fieldnames=("Feature col 1", "Feature col 2", "Feature col n"))

# Parse the CSV into JSON
out = json.dumps([row for row in reader])

f = open('Filename.json', 'w')

f.write(out)

print("JSON saved!")

#run this below command in terminal not in mongodb shell
#to json to csv
#mongoimport --db dbName --collection collectionName --file parsed.json --jsonArray
