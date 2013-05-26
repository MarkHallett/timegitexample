# eg_code.py

import time
import datetime
import random

def eg_func1():
    print datetime.datetime.now()
    time.sleep(2)
    print datetime.datetime.now()

def eg_func2():
    t = random.uniform(1,2)
    print t
    time.sleep(t)
               
               
#if __main__ == '__name__':
#    eg_func()
