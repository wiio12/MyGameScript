import time

from screen import match_until
from utility import *
import loger


def login():
    count = 0
    while True:
        s = match_until(['update', 'main', 'cross', 'notification'])
        if s == 'update':
            loger.log("Need update..")
            tap(840, 557)
        elif s == 'cross':
            tap(1242, 29)
        elif s == 'notification':
            tap(1181, 405)
        elif s == 'main':
            loger.log("Login successful")
            break
        else:
            count += 1
            time.sleep(3)
            if count > 30:
                loger.log("Login failed")
                break
            
    return True