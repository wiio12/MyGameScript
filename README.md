# 安卓游戏脚本

用于 
- fgo
  - 每日登陆
  - 每日抽取免费友情十连
  - 自动打图
- arknight
  - 每日登陆
  - 宿舍换人
  - 自动打图
- pcr
  - 活动推图
  - 地下城

## 使用方法
1. 安装[Android Debug Bridge](https://developer.android.com/studio/command-line/adb), 并且把adb加入到系统环境变量当中。使用命令

    $ adb

   可以启动adb
2. 安装 [`python3`](https://www.python.org/downloads/release/python-383/) 和 [`pip`](https://pypi.org/project/pip/)
3. 安装依赖库
   
    $ pip install -r requirements.txt

4. 运行
     
    $ python main.py [-args]
  
  其中，-args有
  - -arklogin: 登录明日方舟
  - -arkfight：重复打一个本
  - -fgologin：登录Fgo
  - -fgofight：重复打Fgo的一个本
  - -pcrfightdungeon：打公主链接的地下城
  - -pcrfightevent：打公主链接的活动首通
