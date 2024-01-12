from datetime import datetime
import unittest
import sys

sys.path.append("../")

from stock_scraper.Ticker import convert_to_number, split_range, convert_to_datetime, extract_values

"""

Due to the dynamic nature of web scraping, we'll test the 
script against a snapshot of https://stockanalysis.com/

Snapshot: Jan 11th, 2024 @ 9:00 pm

"""

class TestFunctions(unittest.TestCase):
    
    def test_convert_to_number(self):
        
        self.assertEqual(convert_to_number("2.89T"), 2_890_000_000_000)
        self.assertEqual(convert_to_number("-2.89T"), -2_890_000_000_000)
        self.assertEqual(convert_to_number("383.29B"), 383_290_000_000)
        self.assertEqual(convert_to_number("-383.29B"), -383_290_000_000)
        self.assertEqual(convert_to_number("15.29M"), 15_290_000)
        self.assertEqual(convert_to_number("-15.29M"), -15_290_000)

        self.assertEqual(convert_to_number("2,890,000,000,000"), 2_890_000_000_000)
        self.assertEqual(convert_to_number("-2,890,000,000,000"), -2_890_000_000_000)
        self.assertEqual(convert_to_number("383,290,000,000"), 383_290_000_000)
        self.assertEqual(convert_to_number("-383,290,000,000"), -383_290_000_000)
        self.assertEqual(convert_to_number("15,290,000"), 15_290_000)
        self.assertEqual(convert_to_number("-15,290,000"), -15_290_000)

    def test_split_range(self):
        self.assertEqual(split_range("183.62 - 187.05"), (183.62, 187.05))
        self.assertEqual(split_range("0 - 100.00"), (0.00, 100.00))
    
    def test_convert_to_datetime(self):
        self.assertEqual(convert_to_datetime("Jan 12, 2024"), datetime(2024, 1, 12))
        self.assertEqual(convert_to_datetime("Feb 29, 2024"), datetime(2024, 2, 29))
    
    def test_extract_values(self):
        self.assertEqual(extract_values("$0.96 (0.52%)"), (0.96, 0.52))
        self.assertEqual(extract_values("197.85 (+6.61%)"), (197.85, 6.61))
        self.assertEqual(extract_values("197.85 (-6.61%)"), (197.85, -6.61))

if __name__ == "__main__":
    unittest.main()