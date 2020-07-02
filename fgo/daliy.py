import time

from utility.screen import match_until
from utility.utility import *
import utility.loger as loger

def daliy_free_draw():
    is_drawed = False
    match_list = ['main', 'ten_draw', 'free_draw', 'free_draw_2', 'small_close', 'end_draw', 'free_draw_3', 'cross']
    count = 0
    while True:
        s, p = match_until(match_list, require_coor = True)
        if s is not None:
            count = 0
        if s == 'small_close' or s == 'draw_close' or s == 'cross':
            tap(p[0], p[1], w = 0)
        if s == 'main':
            if is_drawed:
                return 0
            tap(1184, 684, w = 0)
            tap(534, 642, w = 0)
        if s == 'ten_draw':
            tap(45, 355, w = 0)
        if s == 'free_draw':
            tap(638, 551)
        if s == 'free_draw_2':
            tap(836, 562, w = 0)
        if s == 'end_draw':
            loger.log("Daily free draw successed")
            is_drawed = True
            tap(100, 39, w = 0)
        if s == 'free_draw_3':
            is_drawed = True
            loger.log("Daily free draw finished")
            tap(100, 39, w = 0)
        else:
            count += 1
            if count > 30:
                loger.log("match_until time out")
                return -1
    return -1
            


        
        
