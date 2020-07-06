import utility.loger as loger
import utility.utility as utility
from pcr import fight


def run_pcr_fight_dungeon(fight_time=10, use_stone=0):
    utility.GAME = 'pcr'
    loger.log("start fight")
    while True:
        #ret = fgo.daliy.daliy_free_draw()
        ret = fight.fight_dungeon(fight_time=fight_time, use_stone=use_stone)
        if ret != 0:
            loger.log("pcr Fight Failed...")
            break
        break
    loger.log("end fight")

def run_pcr_fight_even(fight_time=15, use_stone=0):
    utility.GAME = 'pcr'
    loger.log("start fight")
    while True:
        #ret = fgo.daliy.daliy_free_draw()
        ret = fight.fight_event(fight_time=fight_time, use_stone=use_stone)
        if ret != 0:
            loger.log("pcr Fight Failed...")
            break
        break
    loger.log("end fight")