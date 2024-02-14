import sys
from random import random

import pandas as pd

from FileOperation import FileOperation
from SalesData import SalesData

sales_data = SalesData("YafeNof.csv")
# Task 2 ex 4
print(sales_data.eliminate_duplicates())
# Task 2 ex 5
print(sales_data.calculate_total_sales())
# Task 2 ex 6
print(sales_data._calculate_total_sales_per_month())
# Task 2 ex 7
print(sales_data._identify_best_selling_product())
# Task 2 ex 8
print(sales_data._identify_month_with_highest_sales())
# Task 2 ex 9
print(sales_data.analyze_sales_data())
# Task 2 ex 10
print(sales_data.analyze_sales_data_extended())
# Task 2 ex 11
print(sales_data.calculate_cumulative_sales())
# Task 2 ex 12
print(sales_data.add_90_percent_values_column())
# Task 2 ex 13
sales_data.bar_chart_category_sum()
# Task 2 ex 14
print(sales_data.calculate_mean_quantity())
# Task 2 ex 15
print(sales_data.filter_by_sellings_or_and())
# Task 2 ex 16
print(sales_data.divide_by_2())
# Task 2 ex 17
print(sales_data.calculate_stats({"Total","Price"}))
# Task 7 ex 3
print(sales_data.extract_sales_and_highest_amount("Sidur"))
# Task 7 ex 4
print("Python version:", sys.version)
# Task 7 ex 5
print(sales_data.process_parameters(10, 20, name="John", age=30))
# Task 7 ex 6
data=pd.read_csv("YafeNof.csv")
# Print the first 3 rows
print("First 3 rows:")
print(data.head(3))

# Print the last 2 rows
print("\nLast 2 rows:")
print(data.tail(2))
# Select a random row
random_index = random.randint(0, len(data) - 1)
print("\nRandom row:")
print(data.iloc[random_index])
# Task 7 ex 7
df = pd.read_csv("YafeNof.csv")
numerical_columns = df.select_dtypes(include='number')
# Iterate through all values in the DataFrame
for value in numerical_columns.values.flatten():
    print(value)






