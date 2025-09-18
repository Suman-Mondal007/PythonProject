import pandas as pd
data={
    "Name":['Ram','Shyam'],
    "Age":[22,22],
    "City":['London','Paris']

}
df=pd.DataFrame(data)
print(df)
# df.to_csv('data.csv',index=False)
df.to_excel('data.xlsx',index=False)