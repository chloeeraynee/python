# -*- coding: utf-8 -*-
"""proj2-web_scraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BXTQ-kDJU833oJ8W3b7x_8afzHMjMolY

Using pandas to pull html tables from the web. Based on chapter 2 of 'Princples of Data Science'.
"""

# loading pandas library
import pandas as pd

# reading data from web
house_list = pd.read_html("https://ofm.wa.gov/washington-data-research/statewide-data/washington-trends/economic-trends/median-home-price")
income_list = pd.read_html("https://ofm.wa.gov/washington-data-research/statewide-data/washington-trends/economic-trends/washington-and-us-capita-personal-income")

# transforming list to dataframe
house = house_list[0]
income = income_list[0]

# converting strings to numeric values
house = house.replace('[\D,]', '', regex=True).astype(int)
house.head(5)

income = income.replace('[\D,]', '', regex=True).astype(int)
income

# ploting the two data series on the same plot
import matplotlib.pyplot as pl
pl.figure(figsize=(10,7))
pl.locator_params(nbins=11)
pl.plot(income['Year'], income['Washington'], label='Per Capita Income', color='green')
pl.plot(house['Year'], house['Median'], label='Median Housing Cost', color='red')
pl.title('Washington State Per Capita Income vs. Median Housing Cost')
pl.xlabel('Year')
pl.ylabel('US Dollars')
pl.legend()