import threading
import time


def f():
    print('ran')
    # function's body
    time.sleep(1)
    # whatever else we might want to do
    print('done')
    time.sleep(0.85)
    print('done again')


x = threading.Thread(target=f, args=())  # Now it's created
x.start()  # Now we run it

print(threading.activeCount())  # We get 2 or 4 with the console, the main and the one we just created
                                # The 2 will print while the thread created is sleeping

time.sleep(0.9)  # As sleep is less than the 1 sec sleeps it prints it before 'done'
                # If this sleep was bigger it would print 'done' first
print('finally')

threading.current_thread().getName()  # Para saber el nombre del thread que se está ejecutando