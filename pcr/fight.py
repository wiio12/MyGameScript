import random
from utility.screen import match_until
from utility.utility import *
from utility.loger import log


def fight_event(fight_time=15, use_stone=0):
    while True:
        flag = False
        fight_count = 0
        s, p = match_until(["next_fight", 'start_fight', 'start_fight_2', 'next', 'shop', 'next_1', 'close', 'ap_out'], require_coor=True, cof=0.85)
        if s == 'next_fight':
            tap(p[0], p[1] + 50)
            flag = True
        elif s == 'start_fight' or s == 'start_fight_2':
            tap(1114, 607, w=1)
            if flag:
                fight_count += 1
                flag = False
        elif s == 'next':
            tap(1107, 671, w=4)
        elif s == 'shop':
            tap(498, 492, w=1)
        elif s == 'next_1':
            tap(1107, 671, w=4)
        elif s == 'close':
            tap(p[0], p[1])
        elif s == 'ap_out':
            if use_stone > 0:
                tap(786, 494, w=1)
                tap(786, 494, w=1)
                use_stone -= 1
            else:
                log("体力完了")
                return 0

        if fight_count > fight_time:
            return 0

def fight_dungeon(fight_time=10, use_stone=0):
    while True:
        flag = False
        fight_count = 0
        s, p = match_until(["next_fight_d", 'next_fight_d_2', 'start_fight_d', 'start_fight_2', 'next', 'shop', 'next_1', 'close', 'ok_d'], require_coor=True, cof=0.85)
        if s == 'next_fight_d' or s == 'next_fight_d_2':
            tap(p[0], p[1])
            flag = True
        elif s == 'start_fight_d' or s == 'start_fight_2':
            tap(1114, 607, w=1)
            if flag:
                fight_count += 1
                flag = False
        elif s == 'next':
            tap(1107, 671, w=4)
        elif s == 'shop':
            tap(498, 492, w=1)
        elif s == 'next_1':
            tap(1107, 671, w=4)
        elif s == 'close' or s == 'ok_d':
            tap(p[0], p[1])

        if fight_count > fight_time:
            return 0