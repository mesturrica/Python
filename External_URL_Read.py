import pandas as pd
import urllib3 as lib
import csv

# Read data from a External URL

medals_url = "http://winterolympicsmedals.com/medals.csv"

medals_data = pd.read_csv(medals_url)

print(medals_data.head())

# Done with urllib3
http = lib.PoolManager()
r = http.request('GET',medals_url)

print(r.status)
print(r.data)