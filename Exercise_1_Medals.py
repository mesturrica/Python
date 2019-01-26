import pandas as pd
import urllib3 as lib
import csv
import os

# Read data from a External URL

medals_url = "http://winterolympicsmedals.com/medals.csv"

medals_data = pd.read_csv(medals_url)

print(medals_data.head())

# Done with urllib3
http = lib.PoolManager()
r = http.request('GET',medals_url)

# We need to decode the data, because it's not a string, it's binary
response = r.data
string_data = response.decode("utf-8")

# We divide the string into an array of strings, separated by intro
lines = string_data.split("\n")

# We extract first line, because it's the header
header = lines[0].split(",")
num_col = len(header)

print(string_data)
print(header)
print(num_col)

# We generate an empty dictionary that will contain all the processed data
count = 0
dictionary = {}

for col in header:
    dictionary[col] = []

print(dictionary)

# We process data row by row to fill the dictionary
for line in lines:
    # We don't count first line, it's the header
    if(count > 0):
        values = line.strip().split(",")
        for i in range(len(header)):
            dictionary[header[i]] = values[i]
    count +=1

print(dictionary)

print(count)

# We transform the dictionary into a dataframe
#dataframe_medal = pd.DataFrame(dictionary)
#dataframe_medal.head()

# We store the data in a local folder in the project

path = "Datasets/"

filepath = "Athletes/titanic3."

fullpath = os.path.join(path, filepath)

# We store it in different formats
#dataframe_medal.to_csv(fullpath+"csv")
#dataframe_medal.to_json(fullpath+"json")
#dataframe_medal.to_excel(fullpath+"xls")