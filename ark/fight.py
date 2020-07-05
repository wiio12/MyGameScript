from utility.loger import log
from utility.utility import *
from utility.screen import match_until


def fight(use_san = 0, use_stone = 0):
    count = 0
    fight_count = 0
    fight_flag = False
    while True:
        s = match_until(['start_operation_2', 'start_operation', 'fighting', 'operation_end', 'use_san', 'use_stone'])
        print(s)
        if s is not None:
            count = 0
        if s == 'start_operation':
            tap(1153, 652)
        if s == 'start_operation_2':
            tap(1104, 493)
            fight_flag = True
        if s == 'operation_end':
            tap(1104, 493)
            if fight_flag:
                fight_count += 1
                log("Finish finght: %d" % (fight_count))
                fight_flag = False
            wait(3)
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
            print('count: ', count)
            count += 1
            if count > 30:
                log("fight time out")
                return -1
    return 0
        



