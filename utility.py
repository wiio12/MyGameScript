import time, os
import random

HEIGHT = 720
WIDTH = 1280
global GAME 
GAME = ""

def random_point(x, y):
    x = random.randint(-15, 15) + x
    y = random.randint(-15, 15) + y
    if x < 0: x = 2
    if x > WIDTH: x = WIDTH - 2
    if y < 0: y = 2
    if y > HEIGHT: y = HEIGHT - 2
    return x, y

def tap(x,y):
    x, y = random_point(x, y)
    os.system(f'adb shell input tap {x} {y}')

def swipe(x1, y1, x2, y2):
    x1, y1 = random_point(x1, y1)
    x2, y2 = random_point(x2, y2)
    os.system(f'adb shell input swipe {x1} {y1} {x2} {y2}')

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