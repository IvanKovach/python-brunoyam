import requests
import bs4
import pandas as pd
import matplotlib.pyplot as plt

page = requests.get("http://mfd.ru/currency/?currency=USD")

soup = bs4.BeautifulSoup(page.text, 'lxml')
table = soup.find('table', {'class': 'mfd-table mfd-currency-table'})

historical_data = pd.read_html(str(table))
course = historical_data[0].to_dict(orient='records')
course.reverse()
x, y = [], []
for day_course in course:
    x.append(day_course['Дата'].split()[1])
    y.append(day_course['Курс'])

plt.plot(x, y)
plt.xlabel('Дата')
plt.ylabel('Курс доллара')
plt.title('Доллар США')
plt.show()
