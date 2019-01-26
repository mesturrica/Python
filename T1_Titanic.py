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
