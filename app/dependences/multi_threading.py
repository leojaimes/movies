import threading
import time


# def worker():
#     print("start")
#     time.sleep(2)
#     print("end")


# threads = list()
# for i in range(5):
#     t = threading.Thread(target=worker)
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()


def worker1(iterations):
    list1 = list()
    for i in range(iterations):
        list1.append(i)
        time.sleep(0.01)


time0 = time.time()
worker1(5000)
time1 = time.time()
print(f"time total  in a thread { time1 - time0 } seconds")
