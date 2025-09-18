import pandas as pd
#read data from csv
df=pd.read_csv("suman.csv",encoding="utf-8")
df=pd.read_excel("suman.xlsx")
print(df)