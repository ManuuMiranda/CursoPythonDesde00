import threading
import time


def print_time(thread_name, delay, count):
    while count:
        time.sleep(delay)
        print((thread_name, time.ctime(time.time()), count), '\n')
        count -= 1


class MyOwnThread(threading.Thread):
    def __init__(self, ID, name, delay):
        threading.Thread.__init__(self)
        self.ID = ID
        self.name = name
        self.delay = delay

    def run(self):
        print('Starting' + self.name + '\n')
        print_time(self.name, self.delay, 5)
        print('Exiting' + self.name + '\n')


# First we instantiate the threads
thread0 = MyOwnThread(1, 'Thread 0', 1)
thread1 = MyOwnThread(1, 'Thread 1', 1.5)  # Will finish last because of its larger delay

# Start new threads
thread0.start()
thread1.start()
thread0.join()
thread1.join()

# Watch how the time affects, it is even shown on the prints
print('Exiting main thread')