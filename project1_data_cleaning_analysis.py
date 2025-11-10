import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(r"employee_data_200.csv")

# Display first few rows
print("Initial Data Preview:\n", df.head())

# Check basic info
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

# Remove duplicates if any
df.drop_duplicates(inplace=True)

# Handle missing values (if present)
df.fillna(method='ffill', inplace=True)

# Convert Joining Date to datetime format
df['Joining_Date'] = pd.to_datetime(df['Joining_Date'])

# Display statistical summary
print("\nStatistical Summary:\n", df.describe())

# Department-wise average salary
dept_salary = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:\n", dept_salary)

# Experience vs Salary Analysis Plot
plt.figure()
plt.scatter(df['Experience'], df['Salary'])
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.title('Experience vs Salary')
plt.savefig('experience_vs_salary.png')

# Department Count Plot
plt.figure()
df['Department'].value_counts().plot(kind='bar')
plt.xlabel('Department')
plt.ylabel('Count')
plt.title('Employee Count by Department')
plt.show()
plt.savefig("employees_per_department.png")


# Save cleaned data
df.to_csv('employee_data_cleaned.csv', index=False)

print("\nCleaned dataset saved as 'employee_data_cleaned.csv'")
print("Charts saved as 'experience_vs_salary.png' and 'department_count.png'")
