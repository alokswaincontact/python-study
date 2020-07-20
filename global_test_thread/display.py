import threading
from time import sleep
from config import *

def display_worker():
    """display thread worker function"""
    while True:
        global variable
        print("{} Value {}".format(threading.currentThread().getName(), variable))
        sleep(1)


