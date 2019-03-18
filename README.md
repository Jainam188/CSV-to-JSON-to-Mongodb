# CSV-to-JSON-to-Mongodb
To convert CSV file into JSON file and MONGODB

Follow the Steps:

    1. First you have to read the CSV file 

    2. Then parse that CSV file into JSON file and save it to JSON format

    3. To convert JSON into Mongodb use mongoimport

I have done it.please check following file

csv-to-json-to-mongo.py

Dependencies

1. import csv

2. import json

after getting the JSON file use below command to convert it into mongodb

    mongoimport --db dbName --collection collectionName --file filename.json --jsonArray

Tip: run this command into simple commandprompt, don't run in mongoshell.
