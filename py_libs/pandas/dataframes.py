import pandas as pd

# DataFrame = A two-dimensional labeled data structure with columns of potentially different types
# data frame 1
data = [100,200,300,400,450]
series = pd.Series(data)
print(series)

# data frame 2
data = {'Name' :['Ali','Hassan','Aisha','Sana'],
        'Age' : [23,25,22,24],}
df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data, index=['Employee 1','Employee 2','Employee 3','Employee 4'])
print(df.loc['Employee 2'])# Access by label
print(df.iloc[2])# Access by position
print(df[df['Age']>=24])# filtering
# adding new column
df['Salary'] = [50000,60000,55000,58000]    
print(df)
# adding new row
new_rows = pd.DataFrame([{'Name':'Salman','Age':28,'Salary':65000},
                         {'Name':'Suhail','Age':27,'Salary':60000}],index=['Employee 5','Employee 6'])
df = pd.concat([df,new_rows])
print(df)