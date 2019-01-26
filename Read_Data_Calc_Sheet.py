import pandas as pd

# XLS and XLSX Files ( Second args are file sheet name inside the xls or xlsx file)

main_path = "Datasets/"

filepath = "titanic/titanic3.xls"

titanic2 = pd.read_excel(main_path + filepath,"titanic3")

print(titanic2)

titanic3 = pd.read_excel(main_path + filepath,"titanic3")

print(titanic3)

titanic3.to_csv(main_path + "titanic/titanic_custom2_csv.csv")

titanic3.to_json(main_path + "titanic/titanic_custom2_json.json")