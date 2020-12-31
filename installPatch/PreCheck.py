import psutil
import platform
from datetime import date
import time
import loadConfig
import logging
import cx_Oracle
import win32serviceutil

'''-------------Declaration part ---------------------------------------------------'''
pF = platform.system()
MODULE_NAME = "[Pre-Checker] "
cD = date.today().strftime('%d_%m_%Y')
cT = time.localtime()
current_time = time.strftime("%H_%M_%S", cT)


# Create and Configure log file
LOG_FORMAT = MODULE_NAME + "[%(levelname)s] [%(asctime)s] - %(message)s."
LOG_FINAME = 'appPatchInstall_'+str(cD)+'_'+str(current_time)+'.log'
logging.basicConfig(filename=LOG_FINAME, level=logging.DEBUG, format =LOG_FORMAT)
logger = logging.getLogger()

win_app_service1 = 'OracleServiceO12CR201'
win_app_service2 = 'OracleOraDB12Home1TNSListener'

'''--------------------------------Methods and main functions part --------------'''
'''Function to get the service name'''
def getService(name):
    service = None
    try:
        service = psutil.win_service_get(name)
        service = service.as_dict()
    except Exception as ex:
        logger.error('#ERROR[getService]# ' + str(ex))

    return service

'''Get the current time'''
def getnow():
    cT = time.localtime()
    current_time = time.strftime("%H:%M:%S", cT)
    datetime_object = '['+str(date.today().strftime('%d-%m-%Y')) +' '+str(current_time)+'] '
    return datetime_object
# Below function is not used.
def log(msg):
    f = open(LOG_FINAME,"a+")
    f.write(msg+'\n')
    f.close()
'''---------------------------------Main execution part -----------------------------'''
'''If Windows OS check the status of the services'''
prop = loadConfig.configProps()

logger.info('Operating System: ' + pF)
logger.info('Logfile:  ' + LOG_FINAME)
logger.info('Loading system config properties .... ')
logger.info('Defined Parameters: ' + str(prop))

win_app_serv1 = 'OracleServiceO12CR201'
win_app_serv2 = 'OracleOraDB12Home1TNSListener'

if (__name__ == "__main__") and (pF.__eq__('Windows')):
    try:
        service = getService(prop['win.app.serv1'])
        if service and service['status'] == 'running':
            logger.info(prop['win.app.serv1'] + ' service is running.')
        else:
            logger.info(prop['win.app.serv1'] + ' service is not running.')

        service = getService(prop['win.app.serv2'])
        if service and service['status'] == 'running':
            logger.info(prop['win.app.serv2'] + ' service is running.')
        else:
            logger.info(prop['win.app.serv2'] + ' service is not running.')

            #log(MODULE_NAME + getnow() +  ' Installation files ....')
            logger.info(' Installation files ....')
            logger.info(prop['patch.platform.weblogic'])
            logger.info(prop['patch.platform.help'])
            logger.info(prop['patch.scpoweb.weblogic'])
            logger.info(prop['patch.scpoeweb.help'])

            dbname = prop['database.type']
            logger.info('Database type: ' + dbname)

        if dbname.isupper().__eq__('oracle'):
            logger.info('Get the detail Of '+dbname +' database')
            con_str = prop['db.usrname.scpomgr']+'/'+prop['db.pwd.scpomgr']+'@'+prop['db.hostname']+':'+prop['db.port']+'/'+prop['db.servicename']
            con_str = str(con_str).replace("'",'')
            logger.info('Db connection String: '+ con_str)
            try:
                conn = cx_Oracle.connect(con_str)
                cur = conn.cursor()
                cur.execute('select user_name,full_name,shared_account from WWFMGR.CSM_USER')
                tempvar = cur.fetchall()
                rc = len(tempvar)
                logger.info('Number of records fetched from DB: '+ str(rc))
                if rc > 0:
                    logger.info('There are services running and stoppig them.')
                    for records in tempvar:
                        if records[2] == 1:
                            logger.info('User name: ' + records[0] + 'is active')
                            try:
                                ser_code = win32serviceutil.StopService("ActiveMQ", "in2-1022589lt1")
                                logger.info(ser_code)
                            except Exception as e:
                                logger.error(str(e))
                        else:
                            logger.info('User name: ' + records[0] + 'is in-active')
                else:
                    logger.info('All services are in Stopped state.')
                cur.close()
                conn.close()
            except Exception as ex:
                logger.error(str(ex))
        else:
            logger.info('Get the detail from ' + prop['database.type'] + ' database{else}')

    except Exception as ex:
        logger.error('#[ MainERROR Block ]# '+str(ex))