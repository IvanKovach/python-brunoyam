import time
from threading import Thread


def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


def main():
    t1 = time.time()
    threads = [Thread(target=get_thread, args=("Thread " + str(i+1), )) for i in range(5)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()
    print("Время работы программы с параллельным запуском потоков:", round(time.time() - t1, 2), "секунд")

    t2 = time.time()
    for i in range(5):
        get_thread("Thread " + str(i+1))
    print("Время работы программы с последовательным запуском функции:", round(time.time() - t2, 2), "секунд")


if __name__ == '__main__':
    main()
