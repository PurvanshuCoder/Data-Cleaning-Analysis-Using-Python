# Data-Cleaning-Analysis-Using-Python
 # 🧹📊 Data Cleaning and Analysis Using Python

## 1. 🌱 Introduction

This project focuses on analyzing an Employee Dataset using Python. The aim is to clean the data, handle inconsistencies, and derive meaningful insights through exploratory data analysis. The dataset contains employee information including personal details, work-related attributes, and salary information.

The steps taken in the project ensure that the data becomes accurate, consistent, and ready for analytical interpretation.

## 2. 📂 Dataset Description

The dataset consists of 200 employee records with the following fields:

| Column Name  | Description                                           |
| ------------ | ----------------------------------------------------- |
| ID           | Unique Employee Identifier                            |
| Name         | Employee Full Name                                    |
| Age          | Age of the Employee                                   |
| Department   | Department Assigned                                   |
| Salary       | Monthly Salary                                        |
| Joining_Date | Date when the Employee Joined the Company             |
| Email        | Official Email Address (Contains some missing values) |
| Experience   | Total Work Experience in Years                        |
| Location     | Work Location                                         |

## 3. 🎯 Objectives of the Project

* ✨ Clean the dataset by handling missing or inconsistent values.
* 🔍 Analyze and understand patterns in employee distribution.
* 📊 Visualize data to support interpretation.
* 🧠 Summarize key insights related to employee structure.

## 4. 🧰 Tools and Libraries Used

* 🐍 Python
* 🐼 Pandas
* 🔢 NumPy
* 📈 Matplotlib

## 5. 🧽 Data Cleaning Steps Performed

1. Loaded the dataset into a DataFrame.
2. Checked for data types and corrected formats where needed.
3. Identified missing values and handled them appropriately.
4. Validated that no duplicate entry affected the dataset.
5. Cleaned inconsistent formatting issues in text fields.

## 6. 🔍 Exploratory Data Analysis

* Generated frequency counts of employees in each department.
* Compared experience levels across departments.
* Observed the distribution of salaries.

## 7. 📊 Visual Insight

The following chart shows how employees are distributed across various departments:

![Employees per Department](employees_per_department.png)

This visualization helps understand workforce structure and compare department sizes.

## 8. 💡 Key Insights

* The workforce is not evenly distributed across departments.
* Some departments have significantly more staffing than others, indicating workload or business priorities.
* Missing emails indicate data entry inconsistencies which should be improved in HR registration processes.

## 9. ✅ Conclusion

This project demonstrates how data cleaning and exploratory analysis help in transforming raw data into structured and meaningful information. Proper analysis guides better decision-making and resource planning.

## 10. 🚀 How to Run the Project

1. Place the dataset file and the Python script in the same folder.
2. Run the script using Python.
3. View the output charts and cleaned data results.

```bash
python project_script.py
```

## 11. 🔮 Future Enhancements

* Add more detailed performance and productivity metrics.
* Integrate dashboard visualization tools.
* Automate repeated data cleaning tasks.

