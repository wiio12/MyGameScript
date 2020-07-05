import utility.utility as utility
import utility.loger as loger
from ark import login, fight

def run_ark(user='test', passwd='test', close=True):
    """
    arknights part
    """
    loger.log("starting arknights...")
    utility.GAME = 'ark'
    utility.start_game('com.hypergryph.arknights/com.u8.sdk.U8UnityContext')
    while True:
        ret = login.login(user, passwd)  # input your password here
        if ret != 0:
            loger.log("Arknights Login Failed, quiting...")
            break
        break
    if close:
        utility.stop_game('com.hypergryph.arknights')
        loger.log("ending arknights...\n")

def run_ark_light():
    """
    arkninghts, 只是自动刷单个图
    """
    utility.GAME = 'ark'
    loger.log("start fight")
    while True:
        ret = fight.fight(use_san=0)  # 设置使用理智液和石头的个数
        if ret != 0:
            loger.log("Arknights Fight Failed...")
            break
        break
    loger.log("end fight")