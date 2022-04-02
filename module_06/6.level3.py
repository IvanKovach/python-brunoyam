import requests
import time
from threading import Thread


def get_html(link):
    print(f"Start: {link}")
    data = requests.get(link)
    return data.text


def main():
    data_urls = []
    t1 = time.time()
    urls = ['https://www.google.com', 'https://2ip.ru', 'https://ya.ru', 'https://ru.wikipedia.org',
            'https://brunoyam.com/kontakty']

    threads = [Thread(target=get_html, args=(url, )) for url in urls]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("Время работы программы с параллельным запуском потоков:", round(time.time() - t1, 2), "секунд")

    t2 = time.time()
    for url in urls:
        get_html(url)
    print("Время работы программы с последовательным запуском функции:", round(time.time() - t2, 2), "секунд")

    print(data_urls)


if __name__ == '__main__':
    main()
