import random
from datetime import datetime

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
class SalesDataError(Exception):
    pass
class SalesData:
    def __init__(self, file_path: str):
        try:
            self.data = pd.read_csv(file_path)
        except FileNotFoundError as e:
            timestamp = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            error_msg = f"<EstiElishevaRuth, {timestamp}> File '{file_path}' not found <EstiElishevaRuth>"
            raise SalesDataError(error_msg) from e
        except pd.errors.ParserError as e:
            timestamp = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            error_msg = f"<EstiElishevaRuth, {timestamp}> Error parsing CSV file '{file_path}' <EstiElishevaRuth>"
            raise SalesDataError(error_msg) from e
        except pd.errors.EmptyDataError as e:
            timestamp = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            error_msg = f"<EstiElishevaRuth, {timestamp}> CSV file '{file_path}' is empty <EstiElishevaRuth>"
            raise SalesDataError(error_msg) from e
        except pd.errors.DtypeWarning as e:
            timestamp = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            error_msg = f"<EstiElishevaRuth, {timestamp}> Error reading data types from CSV file '{file_path}' <EstiElishevaRuth>"
            raise SalesDataError(error_msg) from e

    def eliminate_duplicates(self):
        self.data.drop_duplicates(inplace=True)

    def calculate_total_sales(self):
        try:
            total_sales = self.data.groupby('Product')['Total'].sum().reset_index()

            # Bar plot for total sales per product
            plt.figure(figsize=(10, 6))
            plt.bar(total_sales['Product'], total_sales['Total'])
            plt.xlabel('Product')
            plt.ylabel('Total Sales')
            plt.title('Total Sales per Product')
            plt.xticks(rotation=45)
            plt.show()

            return total_sales
        except KeyError as e:
            error_msg = f"<EstiElishevaRuth, {datetime.now().strftime('%d.%m.%Y, %H:%M:%S')}> KeyError: {str(e)} column not found <EstiElishevaRuth>"
            print(error_msg)
            return pd.DataFrame()
    def _calculate_total_sales_per_month(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y')
        self.data['Month'] = self.data['Date'].dt.month
        self.data['Year'] = self.data['Date'].dt.year

        total_sales_per_month = self.data.groupby(['Year', 'Month']).agg({'Total': 'sum'}).reset_index()
        # Line plot for total sales per month
        plt.figure(figsize=(10, 6))
        plt.plot(total_sales_per_month['Month'], total_sales_per_month['Total'], marker='o')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.title('Total Sales per Month')
        plt.xticks(total_sales_per_month['Month'])
        plt.grid(True)
        plt.show()
        return total_sales_per_month
    def _identify_best_selling_product(self):
        best_selling_product = self.data.groupby('Product')['Quantity'].sum().idxmax()
        # Pie chart for best selling product
        sales_by_product = self.data.groupby('Product')['Quantity'].sum()
        plt.figure(figsize=(8, 8))
        plt.pie(sales_by_product, labels=sales_by_product.index, autopct='%1.1f%%')
        plt.title('Distribution of Sales by Product')
        plt.show()
        return best_selling_product

    def _identify_month_with_highest_sales(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y')
        self.data['Month'] = self.data['Date'].dt.month
        self.data['Year'] = self.data['Date'].dt.year

        total_sales_per_month = self.data.groupby(['Year', 'Month']).agg({'Total': 'sum'})
        month_with_highest_sales = total_sales_per_month.idxmax()

        if not month_with_highest_sales.empty:
            highest_months = [m[1] for m in month_with_highest_sales]  # Extract months
            # Box plot for total sales per month
            plt.figure(figsize=(10, 6))
            plt.boxplot(total_sales_per_month.values)
            plt.xlabel('Month')
            plt.ylabel('Total Sales')
            plt.title('Total Sales per Month (Box Plot)')
            plt.xticks(highest_months, [str(m) for m in highest_months])
            plt.show()
        else:
            print("No data available to identify the month with the highest sales.")

        return month_with_highest_sales


    def analyze_sales_data(self):
        best_selling_product = self._identify_best_selling_product()
        month_with_highest_sales = self._identify_month_with_highest_sales()

        return {
            'best_selling_product': best_selling_product,
            'month_with_highest_sales': month_with_highest_sales
        }

    def analyze_sales_data_extended(self):
        total_sales_per_product = self.calculate_total_sales()
        total_sales_per_month = self._calculate_total_sales_per_month()

        min_sales_product = total_sales_per_product['Total'].idxmin()
        average_sales_per_month = total_sales_per_month['Total'].mean()

        analysis_results = self.analyze_sales_data()
        analysis_results['min_sales_product'] = min_sales_product
        analysis_results['average_sales_per_month'] = average_sales_per_month
        sns.barplot(x='Product', y='Total', data=total_sales_per_product)
        plt.title('Bar Plot of Total Sales per Product')
        plt.xticks(rotation=45)
        plt.show()
        return analysis_results

    def calculate_cumulative_sales(self):
        self.data['Date'] = pd.to_datetime(self.data['Date'], format='%d.%m.%Y')
        self.data.sort_values(by='Date', inplace=True)
        self.data['Cumulative_Sales'] = self.data.groupby('Product')['Total'].cumsum()

        # Line plot for cumulative sales over time
        plt.figure(figsize=(10, 6))
        for product, group in self.data.groupby('Product'):
            plt.plot(group['Date'], group['Cumulative_Sales'], label=product)
        plt.xlabel('Date')
        plt.ylabel('Cumulative Sales')
        plt.title('Cumulative Sales Over Time')
        plt.legend()
        plt.show()

        return self.data

    def add_90_percent_values_column(self):
        self.data['90%_Values'] = self.data['Quantity'] * 0.9

        # Bar plot for 90% values column
        plt.figure(figsize=(10, 6))
        plt.bar(self.data.index, self.data['90%_Values'])
        plt.xlabel('Index')
        plt.ylabel('90% Values')
        plt.title('Bar Plot of 90% Values')
        plt.show()

        return self.data

    def bar_chart_category_sum(self):
        product_sum = self.data.groupby('Product')['Quantity'].sum()
        product_sum.plot(kind='bar')
        plt.xlabel('Product')
        plt.ylabel('Quantity')
        plt.title('Sum of Quantities Sold for Each Product')
        plt.show()

    def calculate_mean_quantity(self):
        total_column = self.data['Total'].values

        # Seaborn Box Plot
        sns.boxplot(data=total_column)
        plt.title('Box Plot of Total Column')
        plt.show()

        mean = np.mean(total_column)
        median = np.median(total_column)
        sorted_total_column = np.sort(total_column)
        second_max = sorted_total_column[-2] if len(sorted_total_column) > 1 else None

        return {
            'mean': mean,
            'median': median,
            'second_max': second_max
        }

    def filter_by_sellings_or_and(self):####
        # Condition 1: Number of selling more than 5 or number of selling == 0
        condition_1 = (self.data.groupby('Product')['Quantity'].sum() > 5) | \
                      (self.data.groupby('Product')['Quantity'].sum() == 0)

        # Condition 2: Price above 300 $ and sold less than 2 times
        condition_2 = (self.data.groupby('Product')['Price'].max() > 300) & \
                      (self.data.groupby('Product')['Quantity'].sum() < 2)

        # Apply the conditions
        filtered_products = self.data.groupby('Product').filter(lambda x: condition_1[x.name] or condition_2[x.name])

        # Plot violin plot using filtered data
        sns.violinplot(x='Product', y='Quantity', data=filtered_products)
        plt.title('Violin Plot of Quantity by Product')
        plt.xticks(rotation=45)
        plt.show()

        return filtered_products

    def divide_by_2(self):
        # Check if "Price" column exists
        if "Price" not in self.data.columns:
            print("Error: 'Price' column not found.")
            return None

        # Split the "Price" column by 2 and store the result in a new column "BlackFridayPrice"
        try:
            self.data["BlackFridayPrice"] = self.data["Price"] / 2
        except ZeroDivisionError as e:
            print("Error:", e)
            return None

        # Replace infinite values with NaN
        self.data.replace([float('inf'), float('-inf')], np.nan, inplace=True)

        # Plot scatter plot
        sns.scatterplot(data=self.data, x='Price', y='BlackFridayPrice')
        plt.title('Scatter Plot of Price vs. BlackFridayPrice')
        plt.show()

        return self.data

    def calculate_stats(self, columns: [str] = None):
        stats = {}
        timestamp = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")

        try:
            if columns is None:
                columns = self.data.columns

            for column in columns:

                column_stats = {}
                column_data = self.data[column]

                # Compute maximum
                column_stats['max'] = column_data.max()

                # Compute sum
                column_stats['sum'] = column_data.sum()

                # Compute absolute values
                column_stats['abs'] = column_data.abs().sum()

                # Compute cumulative maximum
                column_stats['cum_max'] = column_data.cummax()

                stats[column] = column_stats
        except KeyError as e:
            error_msg = f"<EstiElishevaRuth, {timestamp}> KeyError: {str(e)} column not found <EstiElishevaRuth>"
            print(error_msg)
        sns.heatmap(self.data.corr(), annot=True, cmap='coolwarm')
        plt.title('Heatmap of Correlation Matrix')
        plt.show()

        return stats, f"<EstiElishevaRuth, {timestamp}>"

    def extract_sales_and_highest_amount(self, product_name: str):
        try:
            # Filter data for the specified product
            product_data = self.data[self.data['Product'] == product_name]

            if product_data.empty:
                print(f"No data available for product '{product_name}'.")
                return None, None, None  # Return None values for all variables

            # Extract the number of sales
            sales_count = product_data['Quantity'].sum()

            # Extract the highest amount paid
            highest_amount = product_data['Total'].max()

            # Generate a random number within the range of sales count and highest amount
            lottery_number = random.randint(sales_count, highest_amount)

            return sales_count, highest_amount, lottery_number
        except KeyError as e:
            error_msg = f"<EstiElishevaRuth, {datetime.now().strftime('%d.%m.%Y, %H:%M:%S')}> KeyError: {str(e)} column not found <EstiElishevaRuth>"
            print(error_msg)
            return None, None, None

    def process_parameters(*args, **kwargs):
        result = {}

        for arg in args:
            if isinstance(arg, (int, float)):
                print(arg)

        for key, value in kwargs.items():
            result[key] = value

        return result