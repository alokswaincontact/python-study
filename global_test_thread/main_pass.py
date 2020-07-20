import threading
from time import sleep
from config import *
#from display import *

#config.variable = "Iovine"

print("File {} Value {}".format(__file__, variable))

def modify_worker():
    """modify thread worker function"""
    while True:
        global variable
        variable += 2
        print("{} Value {}".format(threading.currentThread().getName(), variable))
        sleep(1)

def display_worker():
    """display thread worker function"""
    while True:
        print("{} Value {}".format(threading.currentThread().getName(), variable))
        sleep(1)

tm = threading.Thread(name=" modify", target=modify_worker)
tm.start()
td = threading.Thread(name="display", target=display_worker)
td.start()

x = input("Press Enter to exit\n")
exit(0)
