import requests
import bs4


def tag_td_no_class(tag):
    return tag.name == 'td' and type(tag.contents[0]) == bs4.element.NavigableString


def main():
    page = requests.get("http://mfd.ru/currency/?currency=USD")
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', {'class': 'mfd-table mfd-currency-table'})
    rates = table.find_all(tag_td_no_class)
    rates.reverse()
    dates, courses = [], []

    for rate in rates:
        if 'с' in rate.text:
            dates.append(rate.text.split()[1])
        else:
            courses.append(float(rate.text))
    result = {}
    for i in range(len(dates)):
        result.update({dates[i]: courses[i]})
    print(result)


if __name__ == '__main__':
    main()
