import threading
import time

ls = []


def count(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)


def count2(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)


x = threading.Thread(target=count, args=(10,))
x.start()
x.join()  # .join() indicates the main thread to wait before x stops running, doesn't run y thread until x finishes

y = threading.Thread(target=count2, args=(10,))
y.start()

y.join()  # .join() indicates the main thread to wait before y stops running

print(ls)