import time, os, sys
import random

import utility.utility as utility
import utility.loger as loger
from utility.utility import *
from utility.screen import match_until
import fgo.login, fgo.fight, fgo.daliy
import ark.login, ark.fight


def run_fgo():
    """fgo part"""
    loger.log("starting fgo...")
    utility.GAME = 'fgo'
    start_game('com.bilibili.fatego/jp.delightworks.Fgo.player.AndroidPlugin')
    while True:
        ret = fgo.login.login()
        if ret != 0:
            break
        ret = fgo.daliy.daliy_free_draw()
        if ret != 0:
            break
        break
    stop_game('com.bilibili.fatego')
    loger.log("ending fgo...\n")

def run_ark():
    """
    arknights part
    """
    loger.log("starting arknights...")
    utility.GAME = 'ark'
    start_game('com.hypergryph.arknights/com.u8.sdk.U8UnityContext')
    while True:
        ret = ark.login.login(user = "test", passwd = "test")  # input your password here
        if ret != 0:
            loger.log("Arknights Login Failed, quiting...")
            break
        break

    stop_game('com.hypergryph.arknights')
    loger.log("ending arknights...\n")

def run_ark_light():
    """
    arkninghts, 只是自动刷单个图
    """
    utility.GAME = 'ark'
    loger.log("start fight")
    while True:
        ret = ark.fight.fight(use_san = 0)  # 设置使用理智液和石头的个数
        if ret != 0:
            loger.log("Arknights Fight Failed...")
            break
        break
    loger.log("end fight")

def run_fog_fight():
    utility.GAME = 'fgo'
    loger.log("start fight")
    while True:
        #ret = fgo.daliy.daliy_free_draw()
        ret = fgo.fight.fight(use_gold = 0)
        if ret != 0:
            loger.log("FGO Fight Failed...")
            break
        break
    loger.log("end fight")

if __name__ == "__main__":
    connect_adb()
    if sys.argv[1] == '-fgo':
        s = match_until(['home'])
        if s == 'home':
            run_fgo()
        else:
            loger.log('Error matching [home]')
    
    elif sys.argv[1] == '-ark':
        s = match_until(['home'])
        if s == 'home':
            run_ark()
        else:
            loger.log('Error matching [home]')
    
    elif sys.argv[1] == '-arklight':
        run_ark_light()
    
    elif sys.argv[1] == '-fgofight':
        run_fog_fight()
    
    else:
        loger.log("system parameter error") 
        