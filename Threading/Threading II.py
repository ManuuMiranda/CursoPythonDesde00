import threading
import time


def count(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(0.01)  # sleeps every iteration


for nu in range(2):
    x = threading.Thread(target=count, args=(10,))  # The comma is because its args
    x.start()

print('Printing Done in the main thread')
# This is printed before the rest of the count because we pause in both count threads, it brings us to the main thread