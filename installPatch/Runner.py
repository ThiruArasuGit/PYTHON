import sys, os
MODULE_NAME = "[Runner] "
if (__name__ == "__main__"):
    atNow = PreCheck.getnow()
    try:
       '''
        retcode = subprocess.call([sys.executable, "PreCheck.py"])
        if retcode == 0:
            PreCheck.log(MODULE_NAME + atNow + ' Pre-Check ran successfully')
            #raise Exception('Precheck error')
        else:
            raise Exception('Precheck error')
        '''
       topa = PreCheck.prop['jda.platform.home'].replace("\\","/")
       dirpath = os.getcwd()
       PreCheck.log(MODULE_NAME + atNow + 'Current: ' + dirpath)
       PreCheck.log(MODULE_NAME + atNow + 'sett to: ' +topa)
       os.chdir(topa)
       dirpath = os.getcwd()
       PreCheck.log(MODULE_NAME + atNow + 'NEW: '+dirpath)
    except Exception as err:
        #print(err)
        PreCheck.log(MODULE_NAME + atNow + 'Error# ' + str(err))
        sys.exit(1)



