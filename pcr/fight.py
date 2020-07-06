import random
from utility.screen import match_until
from utility.utility import *
from utility.loger import log


def fight(fight_time=100, use_stone=0):
    while True:
        flag = False
        fight_count = 0
        s, p = match_until(["next_fight", 'start_fight', 'next', 'shop', 'next_1', 'close'], require_coor=True, cof=0.85)
        if s == 'next_fight':
            tap(p[0], p[1] + 50)
            flag = True
        elif s == 'start_fight':
            tap(1114, 607, w=0)
            tap(1114, 607, w=0)
            if flag:
                fight_count += 1
        elif s == 'next':
            tap(1107, 671, w=4)
        elif s == 'shop':
            tap(498, 492, w=1)
        elif s == 'next_1':
            tap(1107, 671, w=4)
        elif s == 'close':
            tap(p[0], p[1])

        if fight_count > fight_time:
            return 0