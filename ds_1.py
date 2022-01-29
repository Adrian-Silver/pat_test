import pandas as pd

d = {"col1": [2, 3, 4, 55, 60], "col2": [3, 5, 7, 42, 31], "col3": [7, 4, 3, 27, 99]}

#  col1, col2, col3 are the names of the columns.

df = pd.DataFrame(data=d)

# .shape[0] gives the count of no. of rows
count_rows = df.shape[0]
# .shape[1] gives the count of no. of columns
count_columns = df.shape[1]

print(df)
print()
print("Number of Rows: " + str(count_rows))
print("Number of Columns: " + str(count_columns))

