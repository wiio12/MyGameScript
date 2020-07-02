import time

from utility.screen import match_until
from utility.utility import *
import utility.loger as loger


def login():
    count = 0
    while True:
        s = match_until(['update', 'main', 'cross', 'notification', 'maintenance'])
        if s is not None:
            count = 0
        if s == 'update':
            loger.log("Need update..")
            tap(840, 557)
        elif s == 'cross':
            for i in range(10):
                tap(1242, 29, w=0)
        elif s == 'notification':
            tap(1181, 405)
        elif s == 'main':
            loger.log("Login successful")
            return 0
        elif s == 'maintenance':
            loger.log("Server under maintenance")
            return -1
        else:
            count += 1
            time.sleep(3)
            if count > 30:
                loger.log("Login failed")
                return -1
            
    return -1