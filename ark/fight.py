from utility.loger import log
from utility.utility import *
from utility.screen import match_until
from utility.screen import match_until_sift

def fight(use_san, use_stone):
    count = 0
    fight_count = 0
    while True:
        s, p = match_until_sift(['start_operation_2', 'start_operation', 'fighting', 'operation_end', 'use_san', 'use_stone'])
        if s == 'start_operation' or s == 'start_operation_2' or s == 'operation_end':
            tap(p[0], p[1])
            if s == 'operation_end':
                fight_count += 1
                log("Finish finght: %d" % (fight_count))
                wait(10)
        elif s == 'fighting':
            wait()
            continue
        elif s == 'use_san':
            if use_san > 0:
                use_san -= 1
                log("use one san")
                tap(1086, 572, w = 3)
            else:
                log("Sanit run out")
                return 0
        elif s == 'use_stone':
            if use_stone > 0:
                use_stone -= 1
                log("use one stone")
                tap(1086, 572, w = 3)
            else:
                log("Sanit run out")
                return 0
        else:
            count += 1
            if count > 30:
                log("fight time out")
                return -1
    return 0
        



