# Without creating a class
import time
import threading
from threading import *



def cal_sqre(num):
    for n in num:
        print()
        time.sleep(1)
        print(' Iron from', threading.current_thread().name)


def cal_cube(num):
    for n in num:
        time.sleep(1)
        print(' Man from', threading.current_thread().name)


ar = [4, 5, 6, 7, 2]

t = time.time()
th1 = threading.Thread(target=cal_sqre, args=(ar,))
th2 = threading.Thread(target=cal_cube, args=(ar,))
th1.start()
th2.start()
th1.join()
th2.join()
print('Bye From', threading.current_thread().name, 'after', time.time() - t, 's')

#By extending the Thread class:

class mythread_a(threading.Thread):
    def run(self):
        for x in range(3):
            time.sleep(1)
            print("Hi from ", self.name)

class mythread_b(threading.Thread):
    def run(self):
        for x in range(3):
            time.sleep(1)
            print("Hi from ", self.name)
t = time.time()
a = mythread_a()
b = mythread_b()
a.start()
b.start()
a.join()
b.join()
print("Bye from",threading.current_thread().name, "after", time.time() - t)

#Without Extending Thread class

class Thread_a:
    def run(self):
        for x in range(5):
            time.sleep(0.5)
            print("Hi from ", current_thread().name)

class Thread_b:
    def run(self):
        for x in range(5):
            time.sleep(0.5)
            print("Hi from ", current_thread().name)

t = time.time()


ta = Thread_a()
tb = Thread_b()

threada = Thread(target=ta.run)
threadb = Thread(target=tb.run)

threada.start()
threadb.start()

threada.join()
threadb.join()

print("done from {} after {}s" .format(current_thread().name, time.time() - t))