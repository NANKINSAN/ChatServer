import threading
import time

class SensorHolder():
    def __init__(self) -> None:
        self.is_sensor = False
        self.t1 = threading.Thread()
        self.interval = Interval(None,None)

    def changeOffDelay(self):
        self.interval.cancel()
        self.interval = Interval(self.changeOff,3)
        self.interval.start()

    def changeOn(self):
        self.is_sensor = True
        self.changeOffDelay()        

    def changeOff(self):
        self.is_sensor = False

    def onSensor(self):
        return self.is_sensor

class Interval():
    def __init__(self,fnc,intervaltime) -> None:
        self.disEnable = False
        self.exefnc = fnc
        self.interval = intervaltime

    def exe(self):
        time.sleep(self.interval)
        if not self.disEnable:
            self.exefnc()

    def start(self):
        t = threading.Thread(target=self.exe)
        t.start()
    
    def cancel(self):
        self.disEnable = True