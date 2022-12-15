import threading
import time


def print_time(thread_name, delay, count):
    while count:
        time.sleep(delay)
        print((thread_name, time.ctime(time.time()), count), '\n')
        count -= 1


class MyOwnThread(threading.Thread):
    def __init__(self, ID, name, count):
        threading.Thread.__init__(self)
        self.ID = ID
        self.name = name
        self.count = count

    def run(self):
        print('Starting:' + self.name + '\n')
        threadlock.acquire()  # Lock the thread and don't let any other thread run until it finishes
        print_time(self.name, 1, self.count)
        threadlock.release()  # Releases the lock, so when run() finishes allows another thread to start running
        print('Exiting:' + self.name + '\n')


# We instantiate a lock
threadlock = threading.Lock()

# Then we instantiate the threads
thread0 = MyOwnThread(1, 'Thread 0', 5)
thread1 = MyOwnThread(1, 'Thread 1', 10)  # Will finish last because of its larger delay

# Start new threads
thread0.start()
thread1.start()
thread0.join()
thread1.join()

# Watch how the time affects, it is even shown on the prints
print('Exiting main thread')