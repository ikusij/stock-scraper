from datetime import datetime
import unittest
import sys

sys.path.append("../")

from stock_scraper.Ticker import Ticker

"""

Due to the dynamic nature of web scraping, we'll test the 
script against a snapshot of https://stockanalysis.com/

Snapshot: Jan 11th, 2024 @ 9:00 pm

"""

class TestClass(unittest.TestCase):

    def test_ticker(self):

        bac = Ticker("BAC")

        self.assertEqual(bac.market_cap, 262_340_000_000)
        self.assertEqual(bac.revenue, 101_150_000_000)
        self.assertEqual(bac.net_income, 28_930_000_000)
        self.assertEqual(bac.shares, 7_910_000_000)
        self.assertEqual(bac.eps, 3.57)
        self.assertEqual(bac.pe, 9.29)
        self.assertEqual(bac.forward_pe, 10.26)
        self.assertEqual(bac.dividend, 0.96)
        self.assertEqual(bac.dividend_percent, 2.90)
        self.assertEqual(bac.dividend_date, datetime(2023, 11, 30))
        self.assertEqual(bac.volume, 48_555_548)
        self.assertEqual(bac.open, 33.36)
        self.assertEqual(bac.prev_close, 33.60)
        self.assertEqual(bac.day_low, 32.78)
        self.assertEqual(bac.day_high, 33.50)
        self.assertEqual(bac.year_low, 24.96)
        self.assertEqual(bac.year_high, 37.00)
        self.assertEqual(bac.beta, 1.42)
        self.assertEqual(bac.forecast, "Buy")
        self.assertEqual(bac.price_target, 36.28)
        self.assertEqual(bac.upside, 9.44)
        self.assertEqual(bac.earnings_date, datetime(2024, 1, 12))

    def test_ticker_new(self):

        roma = Ticker("ROMA")

        self.assertEqual(roma.market_cap, 15_490_000)
        self.assertEqual(roma.revenue, 1_740_000)
        self.assertEqual(roma.net_income, -129_413)
        self.assertEqual(roma.shares, 3_830_000)
        self.assertEqual(roma.eps, -0.03)
        self.assertEqual(roma.pe, None)
        self.assertEqual(roma.forward_pe, None)
        self.assertEqual(roma.dividend, None)
        self.assertEqual(roma.dividend_percent, None)
        self.assertEqual(roma.dividend_date, None)
        self.assertEqual(roma.volume, 40_416_888)
        self.assertEqual(roma.open, 4.18)
        self.assertEqual(roma.prev_close, 3.95)
        self.assertEqual(roma.day_low, 3.95)
        self.assertEqual(roma.day_high, 6.73)
        self.assertEqual(roma.year_low, 2.30)
        self.assertEqual(roma.year_high, 11.80)
        self.assertEqual(roma.beta, None)
        self.assertEqual(roma.forecast, None)
        self.assertEqual(roma.price_target, None)
        self.assertEqual(roma.upside, None)
        self.assertEqual(roma.earnings_date, None)

    def test_ticker_invalid(self):

        appl = Ticker("APPL")

        self.assertEqual(appl.market_cap, None)
        self.assertEqual(appl.revenue, None)
        self.assertEqual(appl.net_income, None)
        self.assertEqual(appl.shares, None)
        self.assertEqual(appl.eps, None)
        self.assertEqual(appl.pe, None)
        self.assertEqual(appl.forward_pe, None)
        self.assertEqual(appl.dividend, None)
        self.assertEqual(appl.dividend_percent, None)
        self.assertEqual(appl.dividend_date, None)
        self.assertEqual(appl.volume, None)
        self.assertEqual(appl.open, None)
        self.assertEqual(appl.prev_close, None)
        self.assertEqual(appl.day_low, None)
        self.assertEqual(appl.day_high, None)
        self.assertEqual(appl.year_low, None)
        self.assertEqual(appl.year_high, None)
        self.assertEqual(appl.beta, None)
        self.assertEqual(appl.forecast, None)
        self.assertEqual(appl.price_target, None)
        self.assertEqual(appl.upside, None)
        self.assertEqual(appl.earnings_date, None)

if __name__ == "__main__":
    unittest.main()