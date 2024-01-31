import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

page = requests.get('https://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')


table = soup.find('table', {'class': 'mfd-currency-table'})
rows = table.find_all('tr')


dates = []
exchange_rates = []


for row in rows[1:]:
    columns = row.find_all('td')
    
    date = columns[0].text.strip()
    exchange_rate = float(columns[1].text.strip().replace(',', '.'))  

    
    dates.append(date)
    exchange_rates.append(exchange_rate)


plt.plot(dates, exchange_rates, marker='o')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.title('USD Exchange Rate Over Time')
plt.xticks(rotation=45)
plt.show()