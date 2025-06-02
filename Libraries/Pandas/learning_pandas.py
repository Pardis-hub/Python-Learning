import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eli'],
    'Age': [25, 30, 35, 40, 20],
    'Salary': [50000, 70000, 60000, 40000, 55000]
}

df = pd.DataFrame(data)
#print(df)

df['Bonus'] = df['Salary'] * 0.1
#print(df)

# Create a MultiIndex DataFrame
arrays = [['Group1', 'Group1', 'Group2', 'Group2'], ['A', 'B', 'C', 'D']]
index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Label'))
df_multi = pd.DataFrame({'Values': [10, 20, 30, 40]}, index=index)

print(df_multi)

# Access data from a specific group
print(df_multi.loc['Group1'])