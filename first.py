import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

page = requests.get('https://mfd.ru/currency/?currency=USD')

soup = BeautifulSoup(page.text, 'html.parser')

currencys = soup.find_all('table', {'class':'mfd-currency-table'})


print([currency.text for currency in currencys])