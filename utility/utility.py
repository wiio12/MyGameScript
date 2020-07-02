import time, os
import random

HEIGHT = 720
WIDTH = 1280
global GAME 
GAME = ""

def random_point(x, y, r = 15):
    x = random.randint(-r, r) + x
    y = random.randint(-r, r) + y
    if x < 0: x = 2
    if x > WIDTH: x = WIDTH - 2
    if y < 0: y = 2
    if y > HEIGHT: y = HEIGHT - 2
    return x, y

def wait(t = 1.0):
    if t < 0:
        return
    t = t + random.random()
    time.sleep(t)

def connect_adb():
    os.system('adb connect 127.0.0.1:7555')

def start_game(game):
    os.system(f'adb shell am start -n {game}')

def stop_game(game):
    os.system(f'adb shell am force-stop {game}')

def text(msg, w = -1):
    wait(w / 2.0)
    os.system(f'adb shell input text {msg}')
    wait(w / 2.0)

def tap(x,y, w = -1, r = 15):
    wait(w / 2.0)
    x, y = random_point(x, y, r = r)
    os.system(f'adb shell input tap {x} {y}')
    wait(w / 2.0)

def swipe(x1, y1, x2, y2, w = -1, r = 15):
    wait(w / 2.0)
    x1, y1 = random_point(x1, y1, r = 15)
    x2, y2 = random_point(x2, y2, r = 15)
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