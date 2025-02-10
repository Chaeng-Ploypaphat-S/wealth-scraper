import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all elements with the specified class
        class_name = "whitespace-nowrap px-0.5 py-[1px] text-left text-smaller font-semibold tiny:text-base xs:px-1 sm:py-2 sm:text-right sm:text-small"
        elements = soup.find_all(class_=class_name)

        # Print the text of each element
        for element in elements:
            text = element.get_text()
            if text[0] == "$":
                print('dividend: ', text)
            
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        

def read_trending():
    with open('input_trending/data.csv', mode='r') as file:
        stock_tickers = file.readlines()
        for ticker in stock_tickers:
            url = 'https://stockanalysis.com/stocks/' + ticker
            scrape_website(url)


if __name__ == "__main__":
    read_trending()