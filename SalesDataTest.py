import unittest
from unittest.mock import patch
from SalesData import SalesData, SalesDataError
import pandas as pd

class TestSalesData(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_data.csv"  # Adjust path to your test data CSV file

    @patch('builtins.print')
    def test_init_file_not_found(self, mock_print):
        with self.assertRaises(SalesDataError):
            sales_data = SalesData("non_existent_file.csv")
            mock_print.assert_called_once()

    @patch('builtins.print')
    def test_init_parser_error(self, mock_print):
        with self.assertRaises(SalesDataError):
            sales_data = SalesData("invalid_data.csv")
            mock_print.assert_called_once()

    def test_eliminate_duplicates(self):
        sales_data = SalesData("YafeNof.csv")
        sales_data.eliminate_duplicates()
        self.assertEqual(len(sales_data.data), len(pd.unique(sales_data.data.index)))

    @patch('builtins.print')
    def test_calculate_total_sales(self, mock_print):
        sales_data = SalesData("YafeNof.csv")
        total_sales = sales_data.calculate_total_sales()
        self.assertIsInstance(total_sales, pd.DataFrame)
        self.assertTrue('Product' in total_sales.columns)
        self.assertTrue('Total' in total_sales.columns)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_identify_best_selling_product(self, mock_print):
        sales_data = SalesData("YafeNof.csv")
        best_selling_product = sales_data._identify_best_selling_product()
        self.assertIsInstance(best_selling_product, str)
        mock_print.assert_not_called()

    @patch('builtins.print')
    def test_identify_month_with_highest_sales(self, mock_print):
        sales_data = SalesData("YafeNof.csv")
        month_with_highest_sales = sales_data._identify_month_with_highest_sales()
        self.assertIsInstance(month_with_highest_sales, pd.Series)
        mock_print.assert_not_called()

    # Add more test cases for other methods as needed

if __name__ == '__main__':
    unittest.main()