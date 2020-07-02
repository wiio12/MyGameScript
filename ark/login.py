from utility.loger import log
from utility.utility import *
from utility.screen import match_until
from utility.screen import match_until_sift

def login(user = "", passwd = ""):
    count = 0
    while True:
        s = match_until([ 'login', 'cross', 'main', 'login_1'])
        if s == "loading":
            continue
        elif s == 'login_1':
            tap(644, 502, w = 2)
            tap(645, 595, w = 2)
        elif s == 'login':
            tap(421, 507)
            while True:
                x = match_until(['login_2', 'login_error'])
                if x == 'login_2':
                    tap(638, 425, w = 0.5) # 用户名输入框
                    text(user, w = 0.5)    # 输入用户名
                    tap(348, 409, w = 0.5) # 确认输入
                    tap(640, 476, w = 0.5) # 密码输入框
                    text(passwd, w = 0.5)  # 输入密码
                    tap(345, 434, w = 0)    # 确认输入
                    tap(640, 574)             # 点击登录
                elif x == 'login_error':
                    log("Username or password error...")
                    return -1
                else:
                    break
        elif s == 'cross':
            x, p = match_until_sift(['cross'])
            if x == 'cross':
                tap(p[0], p[1], r = 5)
        elif s == 'main':
            log("Login successful")
            return 0
        else:
            count += 1
            if count >= 30:
                log("login in time out")
                return -1
    return -1
        


        


