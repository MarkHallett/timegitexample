# eg_code.py
''' Example code to show timings
'''

import time
import datetime
import random

def eg_func1():
    '''
    function to cause a delay.
    '''
    print datetime.datetime.now()
    time.sleep(3)
    print datetime.datetime.now()

def eg_func2():
    #t = random.uniform(1,2)
    t = 0
    print t
    time.sleep(t)
               
               
if __name__ == '__main__':
    eg_func1()
    eg_func2()
    
    
