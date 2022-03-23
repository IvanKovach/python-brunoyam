import time
from threading import Thread


def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


def main():
    threads = [Thread(target=get_thread, args=("Thread " + str(i+1), )) for i in range(5)]
    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()
