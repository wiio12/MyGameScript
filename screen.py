import time, os, subprocess
import aircv as ac
import loger 

from utility import *


def match(features_path, cof = 0.9):
    confidence = 0.0
    answer = ""
    subprocess.call('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    subprocess.call('adb pull /sdcard/screenshot.png ./screenshot.png', stdout=subprocess.PIPE)
    imsrc = ac.imread("screenshot.png")
    for f in features_path:
        imsch = ac.imread(f)
        find = ac.find_template(imsrc, imsch)
        if find and find["confidence"] > confidence:
            confidence = find['confidence']
            answer = get_feature(f)
    if confidence < cof:
        return False, 'no match', confidence
    else:
        return True, answer, confidence

def match_until(features, cof = 0.9):
    features_path = get_features_path(features)
    count = 0
    while True:
        count += 1
        if count > 150:
            loger.log("match until failed")
            break
        time.sleep(random.random())
        ret, find, _ = match(features_path, cof)
        if ret:
            break
        tap(random.randint(200, 500), 
            random.randint(200, 500))
        
    return find
        