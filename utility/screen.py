import time
import subprocess
import aircv as ac


from utility.utility import *
import utility.loger as loger

def match(features_path, cof=0.9):
    confidence = 0.0
    answer = ""
    point = None
    subprocess.call('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
    subprocess.call('adb pull /sdcard/screenshot.png ./screenshot.png', stdout=subprocess.PIPE)
    imsrc = ac.imread("screenshot.png")
    for f in features_path:
        imsch = ac.imread(f)
        find = ac.find_template(imsrc, imsch)
        # print(get_feature(f), find)
        if find and find["confidence"] > confidence:
            confidence = find['confidence']
            answer = get_feature(f)
            point = find['result']
    if confidence < cof:
        return False, 'no match', confidence, point
    else:
        return True, answer, confidence, point

def match_until(features, cof=0.9, rand_tap=True, require_coor=False, tap_coor=None, retry_count=150):
    features_path = get_features_path(features)
    count = 0
    while True:
        count += 1
        if count > retry_count:
            loger.log("match until failed")
            break
        wait(1)
        ret, find, _, p = match(features_path, cof)
        if ret:
            break
        if rand_tap and tap_coor is not None:
            tap(tap_coor[0], tap_coor[1])
        elif rand_tap:
            tap(random.randint(530, 730),
                random.randint(260, 380))
        
    if require_coor:
        return find, p
    return find
        