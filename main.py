import time, os
import random

import loger, utility
from utility import *
from screen import match_until
import fgo.login


def run_fgo():
    loger.log("starting fgo...")
    utility.GAME = 'fgo'
    os.system('adb shell am start -n com.bilibili.fatego/jp.delightworks.Fgo.player.AndroidPlugin')
    while True:
        ret = fgo.login.login()
        if ret:
            break
    os.system('adb shell am force-stop com.bilibili.fatego')
    loger.log("ending fgo...\n")

def run_ark():
    loger.log("starting arknights...")
    
    loger.log("ending arknights...\n")

if __name__ == "__main__":
    x = match_until(['home'])
    if x == 'home':
        run_fgo()


    else:
        loger.log('Error matching [home]')
        