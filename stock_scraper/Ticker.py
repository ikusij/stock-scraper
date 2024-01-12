from decimal import Decimal, getcontext
from collections import defaultdict
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import re

def convert_to_number(val: str) -> int:

    """
    
    Helper function that converts a string representation
    of a number into an integer representation.

    The function is able to handle strings that use power
    of ten shorthands (e.g. T for Trillion) or that use 
    commas for legibility.

    @param `str val`: the number string representation.
    
    """

    conversions = { "T": 1e12, "B": 1e9, "M": 1e6 }
    pattern = r"(\-?[0-9]+\.?[0-9]+)([a-zA-Z]+)?"
    match = re.search(pattern, val.replace(",", ""))

    if match.group(2) != None:
        getcontext().prec = 10
        return int(Decimal(match.group(1)) * Decimal(conversions[match.group(2)]))
    
    return int(match.group(1))

def split_range(val: str) -> tuple[float, float]:

    """
    
    Helper function that splits a range into
    two independent values.

    @param `str val`: the value range we want to split.
    
    """
    
    range = val.split(" - ")
    return (float(range[0]), float(range[1]))

def convert_to_datetime(val: str) -> datetime:

    """
    
    Helper function that turns a string date into a datetime object.

    The function converts a string date representation 
    in the "%b %d, $Y" format, which means 
    (shorthand month) (date), (year). 

    @param `str val`: the date string representation of the date to convert.
    
    """

    return datetime.strptime(val, "%b %d, %Y")

def extract_values(val: str) -> tuple[float, float]:

    """
    
    Helper function that extracts the absolute and percentage
    values of a string in the following format "abs (percentage)".

    @param `str val`: string that values will be extracted from. 
    
    """
    
    pattern = r'\$?(\d+\.\d+)\s*\(([+-]?\d+\.\d+)%\)'
    match = re.search(pattern, val)
    
    return (float(match.group(1)), float(match.group(2)))

class Ticker:

    def __init__(self, ticker: str):
        self.ticker = ticker.upper()
        self.invalid_ticker = True
        self._extract_metrics()
        
    def _get_overview_metrics(self) -> defaultdict:

        """
        
        Helper function that scrapes the Overview data for the given ticker.
        
        """
        
        url = f"https://stockanalysis.com/stocks/{self.ticker.lower()}/"
        response = requests.get(url)
        content = response.text

        metrics = defaultdict(lambda: "n/a")

        if "Page Not Found - 404" not in content:
            
            self.invalid_ticker = False

            soup = BeautifulSoup(content, "lxml")

            rows = soup.find_all("tr")
            for row in rows:
                metric, val = row.find_all("td")
                metrics[metric.text.strip()] = val.text.strip()
        
        return metrics
    
    def _extract_metrics(self):

        """

        Helper function that converts the metrics scraped from the website 
        and processes them into the desired types and assigns them to 
        the corresponding member variables.        
        
        """

        metrics = self._get_overview_metrics()
        
        market_cap = metrics["Market Cap"]
        self.market_cap = convert_to_number(market_cap) if market_cap != "n/a" else None

        revenue = metrics["Revenue (ttm)"]
        self.revenue = convert_to_number(revenue) if revenue != "n/a" else None

        net_income = metrics["Net Income (ttm)"]
        self.net_income = convert_to_number(net_income) if net_income != "n/a" else None

        shares = metrics["Shares Out"]
        self.shares = convert_to_number(shares) if shares != "n/a" else None

        eps = metrics["EPS (ttm)"]
        self.eps = float(eps) if eps != "n/a" else None

        pe = metrics["PE Ratio"]
        self.pe = float(pe) if pe != "n/a" else None

        forward_pe = metrics["Forward PE"]
        self.forward_pe = float(forward_pe) if forward_pe != "n/a" else None

        dividend = metrics["Dividend"]
        self.dividend, self.dividend_percent = extract_values(dividend) if dividend != "n/a" else (None, None)

        dividend_date = metrics["Ex-Dividend Date"]
        self.dividend_date = convert_to_datetime(dividend_date) if dividend_date != "n/a" else None

        volume = metrics["Volume"]
        self.volume = convert_to_number(volume) if volume != "n/a" else None

        open = metrics["Open"]
        self.open = float(open) if open != "n/a" else None

        prev_close = metrics["Previous Close"]
        self.prev_close = float(prev_close) if prev_close != "n/a" else None

        days_range = metrics["Day's Range"]
        self.day_low, self.day_high = split_range(days_range) if days_range != "n/a" else (None, None)

        years_range = metrics["52-Week Range"]
        self.year_low, self.year_high = split_range(years_range) if years_range != "n/a" else (None, None)

        beta = metrics["Beta"]
        self.beta = float(beta) if beta != "n/a" else None

        forecast = metrics["Analysts"]
        self.forecast = forecast if forecast != "n/a" else None

        price_target = metrics["Price Target"]
        self.price_target, self.upside = extract_values(price_target) if price_target != "n/a" else (None, None)

        earnings_date = metrics["Earnings Date"]
        self.earnings_date = convert_to_datetime(earnings_date) if earnings_date != "n/a" else None

appl = Ticker("appl")