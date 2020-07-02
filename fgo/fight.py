import random
from utility.screen import match_until, match_until_sift
from utility.utility import *
from utility.loger import log


POINTS_NORMAL = [(135, 508), (386, 508), (656, 508),(900,508),(1160, 508)]
POINTS_BIG = [(386, 245), (656, 245), (900, 245)]

def fight(fight_time = 100, use_white = 0, use_gold = 0, use_stone = 0):
    fight_count = 0
    while True:
        if fight_count > fight_time:
            return 0
        s = match_until(['fight_1', 'assis_choice', 'start_fight', 'attack', 'attack_2','next', 'ap_out', 'story', 'data_update', 'data_update_2'])
        print(s)
        if s == 'story':
            tap(1192, 36, w = 1)
            tap(826, 556)
        if s == 'data_update' or s == 'data_update_2':
            tap(437, 559)
        if s == 'fight_1':
            fight_count += 1
            log("Fight %d" % fight_count)
            tap(943, 234, w = 1)
        if s == 'assis_choice':
            tap(667, 287, w = 1)
        if s == 'start_fight':
            tap(1189, 670, w = 0)
        if s == 'attack':
            tap(1136, 591, w = 1)
        if s == 'attack_2':
            random.shuffle(POINTS_BIG)
            for ps in POINTS_BIG:
                tap(ps[0], ps[1])
            random.shuffle(POINTS_NORMAL)
            for i in range(3):
                tap(POINTS_NORMAL[i][0], POINTS_NORMAL[i][1])
        if s == 'next':
            tap(1112, 675)
        if s == 'ap_out':
            Flag = True
            if use_white > 0:
                tap(688, 475, w = 0)
                x, xp = match_until_sift(['ap_out_1'])
                if x == 'ap_out_1':
                    use_white -= 1
                    Flag = False
                    tap(xp[0], xp[1], w = 1)
                    log("use one white apple")
                else:
                    log("white apple runs out")
            if Flag and use_gold > 0:
                tap(688, 315, w = 0)
                x, xp = match_until_sift(['ap_out_1'])
                if x == 'ap_out_1':
                    use_white -= 1
                    Flag = False
                    tap(xp[0], xp[1], w = 1)
                    log("use one gold apple")
                else:
                    log("gold apple runs out")
            if Flag and use_stone > 0:
                tap(688, 175, w = 0)
                x, xp = match_until_sift(['ap_out_1'])
                if x == 'ap_out_1':
                    use_white -= 1
                    Flag = False
                    tap(xp[0], xp[1], w = 1)
                    log("use one stone apple")
                else:
                    log("gold apple runs out")
            if Flag:
                log("ap runs out, quit...")
                return 0
            





        
    return -1
