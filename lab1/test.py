import requests
import pandas as pd 
from bs4 import BeautifulSoup as bs4

def get_data():
    url = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
    response = requests.get(url)
    soup = bs4(response.text, 'html.parser')
    table = soup.find_all('table')[2]  # The third table on the page
    df = pd.read_html(str(table))
    return df[0]

def main():
    data = get_data()
    print(data.head())

if __name__ == "__main__":
    main()