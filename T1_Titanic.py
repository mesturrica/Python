import pandas as pd
import os

main_path = "Datasets/"

filepath = "titanic/titanic3.csv"


data = pd.read_csv(main_path + filepath, sep = ',', dtype=None)

#See first 5 rows
print(data.head())
print(filepath)


#Another Example
data_cols = pd.read_csv(main_path + "customer-churn-model/Customer Churn Columns.csv")
data_cols_list = data_cols["Column_Names"].tolist()
data2  = pd.read_csv(main_path + "customer-churn-model/Customer Churn Model.txt", names=data_cols_list, header=None)



print(data2.columns.values)


#Open Function

data3 = open(main_path + "customer-churn-model/Customer Churn Model.txt","r")
cols = data3.readline().strip().split(',')

n_cols = len(cols)

counter = 0

main_dict = {}

print(data3)

print(cols)

print(n_cols)

for col in cols:
    main_dict[col] = {}


for line in data3:
    values = line.strip().split(',')
    for i in range(len(cols)):
        main_dict[cols[i]] = (values[i])
    counter +=1

print(main_dict)

#Write on a file

infile = open(main_path + "customer-churn-model/Customer Churn Model.txt")
outfile = open(main_path + "customer-churn-model/Tab Customer Churn Model.txt")

with data3 as infile1:
    with open(outfile,'w') as outfile1:
        for line in infile1:
            fields = line.strip().split(',')
            outfile1.write("/t".join(fields))