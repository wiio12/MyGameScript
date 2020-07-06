import sys
import json


import utility.utility as utility
import utility.loger as loger
import fgo.control
import ark.control
import pcr.control


if __name__ == "__main__":
    config_file = open('./config.json')
    config = json.load(config_file)
    utility.connect_adb(config['emulator'], config['adb_port'])

    if len(sys.argv) < 2:
        loger.log('parameter error')
    elif sys.argv[1] == '-fgo':
        fgo.control.run_fgo()
    elif sys.argv[1] == '-fgofight':
        fgo.control.run_fgo_fight()
    elif sys.argv[1] == '-ark':
        ark.control.run_ark(user=config['arknight_username'], passwd=config['arknight_password'])
    elif sys.argv[1] == '-arkfight':
        ark.control.run_ark_light()
    elif sys.argv[1] == '-pcrfight':
        pcr.control.run_pcr_fight()
    else:
        loger.log("system parameter error")
    
    if len(sys.argv) == 3:
        if sys.argv[2] == '-c':
            utility.close_adb(config['emulator'])