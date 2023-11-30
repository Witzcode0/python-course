import pandas as pd

data = {
    'emp_id': ['#001', '#002', '#003', '#004', '#005', '#006', '#007', '#008', '#009', '#010', '#011', '#012', '#013', '#014', '#015'],
    'name': ['brijesh', 'eric', 'alice', 'david', 'emma', 'frank', 'grace', 'henry', 'irene', 'jason', 'kate', 'leo', 'mia', 'nathan', 'olivia'],
    'age': [28, 35, 22, 40, 29, 45, 32, 38, 26, 33, 28, 41, 27, 36, 31],
    'department': ['HR', 'IT', 'Marketing', 'Finance', 'IT', 'IT', 'Engineering', 'Legal', 'Customer Service', 'Research', 'Product Management', 'Quality Assurance', 'Design', 'Analytics', 'Public Relations'],
    'salary': [50000, 70000, 45000, 80000, 60000, 90000, 55000, 75000, 48000, 82000, 51000, 78000, 52000, 74000, 56000]
}

df = pd.DataFrame(data)

# xlsx_file = df.to_excel('employee.xlsx', index=False)
# print(xlsx_file)

# select all columns
# print(df)

# select single column
# print(df['name'])
# print(type(df['name']))

# select multiple column
# print(df[['emp_id', 'name']])

# Filter rows
# print(df[df['salary'] >= 50000] )
# print(df[df['department'] == 'IT'] )

# Top N row
# print(df.head(7))

# Last N row
# print(df.tail(7))

# Distinct values
# print(df.department.unique())
# print(df.department.nunique())
# print(set(df['department'].tolist()))


# Count of total values
# print(df.size)

# structure of table
# print(df.info())

# sort by single column
# default asending order
# sorted_df = df.sort_values(by=['department'])

# In desending oreder
# sorted_df = df.sort_values(by=['department'], ascending=False)

# print(sorted_df)


# sort by multiple column

# sorted_df = df.sort_values(by=['department', 'age'])

# print(sorted_df)

# sorted_df = df.sort_values(by=['salary'])

# xlsx_file = sorted_df.to_excel('sort_salary_employee.xlsx', index=False)
# print(xlsx_file)