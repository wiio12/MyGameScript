import os
from datetime import datetime

log_file = "./log/log_%s.txt" % (datetime.now().strftime("%d_%m_%Y_%H_%M") )

def log(msg):
    print(log_file)
    with open(log_file, 'a') as f:
        msg = "[%s] %s\n" % ( datetime.now().strftime("%H:%M"), msg)
        print(msg)
        f.write(msg)