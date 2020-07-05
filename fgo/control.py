import utility.loger as loger
import utility.utility as utility
from fgo import daliy, fight, login

def run_fgo():
    """fgo part"""
    loger.log("starting fgo...")
    utility.GAME = 'fgo'
    utility.start_game('com.bilibili.fatego/jp.delightworks.Fgo.player.AndroidPlugin')
    while True:
        ret = login.login()
        if ret != 0:
            break
        ret = daliy.daliy_free_draw()
        if ret != 0:
            break
        break
    utility.stop_game('com.bilibili.fatego')
    loger.log("ending fgo...\n")

def run_fgo_fight(fight_time=100, use_white=0, use_gold=0, use_stone=0):
    utility.GAME = 'fgo'
    loger.log("start fight")
    while True:
        #ret = fgo.daliy.daliy_free_draw()
        ret = fight.fight(fight_time=fight_time, use_white=use_white, use_gold=use_gold, use_stone=use_stone)
        if ret != 0:
            loger.log("FGO Fight Failed...")
            break
        break
    loger.log("end fight")