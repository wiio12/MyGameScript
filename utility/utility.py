import time
import os
import re
import random
import subprocess
import psutil

import utility.loger as loger

HEIGHT = 720
WIDTH = 1280
global GAME 
GAME = ""

def random_point(x, y, r=15):
    x = random.randint(-r, r) + x
    y = random.randint(-r, r) + y
    if x < 0: x = 2
    if x > WIDTH: x = WIDTH - 2
    if y < 0: y = 2
    if y > HEIGHT: y = HEIGHT - 2
    return x, y

def wait(t=1.0):
    if t < 0:
        return
    t = t + random.random()
    time.sleep(t)

def connect_adb(emulator, port):
    # open emulator if not
    emulator_name = emulator.split('/')[-1].split('.')[-2]
    emulator_path = emulator[0 : emulator.find(emulator_name)]
    process = [p.name() for p in psutil.process_iter()]
    if emulator_name + '.exe' in process:
        loger.log("emulator already opened")
    else:
        loger.log("try open emulator")
        cwd = os.getcwd()
        print(emulator, emulator_path, emulator_name)
        os.chdir(emulator_path)
        subprocess.run(['start', './{}.exe'.format(emulator_name)], shell=True, check=True)
        os.chdir(cwd)
        wait(60)
    
    # connect to adb
    subprocess.run('adb kill-server', check=True)
    subprocess.run('adb devices', check=True)
    if int(port) >= 5555 and int(port) <= 5585:
        return
    subprocess.run('adb connect 127.0.0.1:{}'.format(port), check=True)

def close_adb(emulator):
    emulator_name = emulator.split('/')[-1].split('.')[-2]
    process = [p.name() for p in psutil.process_iter()]
    subprocess.run('adb kill-server', check=True)
    closed = []
    for p in process:
        if emulator_name in p and p not in closed:
            subprocess.run('taskkill /IM {} /F'.format(p), check=True)
            closed.append(p)



def start_game(game):
    os.system(f'adb shell am start -n {game}')

def stop_game(game):
    os.system(f'adb shell am force-stop {game}')

def text(msg, w = -1):
    wait(w / 2.0)
    os.system(f'adb shell input text {msg}')
    wait(w / 2.0)

def tap(x, y, w=-1, r=15):
    wait(w / 2.0)
    x, y = random_point(x, y, r=r)
    subprocess.call(f'adb shell input tap {x} {y}')
    wait(w / 2.0)

def swipe(x1, y1, x2, y2, w=-1, r=15):
    wait(w / 2.0)
    x1, y1 = random_point(x1, y1, r=15)
    x2, y2 = random_point(x2, y2, r=15)
    os.system(f'adb shell input swipe {x1} {y1} {x2} {y2}')
    wait(w / 2.0)


def set_game(game):
    GAME = game

def get_features_path(features):
    ret = []
    for f in features:
        if GAME != '':
            ret.append("./" + GAME +"_features/" + f + '.png')
        else:
            ret.append("./features/" + f + ".png")
    return ret

def get_feature(feature_path):
    return feature_path.split('/')[-1].split('.')[0]