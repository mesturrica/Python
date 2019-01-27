import pandas as pd
import os

main_path = "Datasets/"
filepath = "titanic/titanic3.csv"

data = pd.read_csv(os.path.join(main_path, filepath))

# Dummy Variables
print(data["sex"])

dummy_sex = pd.get_dummies(data["sex"], prefix="sex")

print(dummy_sex.head())

column_name = data.columns.values.tolist()

print(column_name)

# We drop the column because we want to put the two dummy variables.
data.drop(["sex"],axis=1)

data2 = pd.concat([data, dummy_sex], axis=1)
print(data2)

# Optimized way
def createDummies(df, varName):
    dummy = pd.get_dummies(df[varName], prefix=varName)
    df.drop([varName], axis = 1)
    df = pd.concat([df, dummy], axis=1)
    return df

print("Function")
print(createDummies(data, "sex"))


