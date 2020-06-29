import time, os, sys
import random

import utility.utility as utility
import utility.loger as loger
from utility.utility import *
from utility.screen import match_until
import fgo.login
import ark.login, ark.fight


def run_fgo():
    """fgo part"""
    loger.log("starting fgo...")
    utility.GAME = 'fgo'
    start_game('com.bilibili.fatego/jp.delightworks.Fgo.player.AndroidPlugin')
    while True:
        ret = fgo.login.login()
        if ret:
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
        ret = ark.fight.fight(use_san = 1, use_stone = 0)  # 设置使用理智液和石头的个数
        if ret != 0:
            loger.log("Arknights Fight Failed...")
            break
        break
    loger.log("end fight")

if __name__ == "__main__":
    if sys.argv[1] == '-fgo':
        s = match_until(['home'])
        if s == 'home':
            run_fgo()
        else:
            loger.log('Error matching [home]')
    
    elif sys.argv[1] == '-arklight':
        run_ark_light()
    
    else:
        loger.log("system parameter error") 
        