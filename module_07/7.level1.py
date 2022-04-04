import requests
import bs4
import pandas as pd

page = requests.get("http://mfd.ru/currency/?currency=USD")

soup = bs4.BeautifulSoup(page.text, 'lxml')
table = soup.find('table', {'class': 'mfd-table mfd-currency-table'})

historical_data = pd.read_html(str(table))
course = historical_data[0].to_dict(orient='records')
[print(day_course) for day_course in course]
