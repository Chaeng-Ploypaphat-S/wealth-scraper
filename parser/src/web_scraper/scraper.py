import csv
import logging
import os
import requests
from bs4 import BeautifulSoup

def scrape_website(stock_symbol):
    url = 'https://stockanalysis.com/stocks/' + stock_symbol
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        class_name = "whitespace-nowrap px-0.5 py-[1px] text-left text-smaller font-semibold tiny:text-base xs:px-1 sm:py-2 sm:text-right sm:text-small"
        elements = soup.find_all(class_=class_name)

        for element in elements:
            specified_dividend = element.get_text()
            if specified_dividend[0] == "$":
                logging.info('%s: dividend: %s', stock_symbol, specified_dividend)
                print('%s: dividend: %s' % (stock_symbol, specified_dividend))
            
    else:
        logging.info("Failed to retrieve the webpage. Status code: %s", response.status_code)
        

def read_trending():
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
    file_path = os.path.join(parent_dir, 'data/dividend_input/data.csv')
    
    target_stocks = []
    with open(file_path, mode='r', encoding='utf-8-sig') as file:
        stock_tickers = csv.reader(file)
        for ticker in stock_tickers:
            # Assume the 1st column contains the stock tickers
            # Later, as the number of columns increase, we can add a loop to iterate over all columns
            stock_symbol = ticker[0]
            target_stocks.append(stock_symbol)
            
    for stock_symbol in target_stocks:
        scrape_website(stock_symbol)


if __name__ == "__main__":
    read_trending()