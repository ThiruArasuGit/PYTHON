from datetime import date
import time

class allFuncs:
    def getnow(_self):
        cT = time.localtime()
        current_time = time.strftime("%H:%M:%S", cT)
        datetime_object = '[' + str(date.today().strftime('%d-%m-%Y')) + ' ' + str(current_time) + '] '
        return datetime_object