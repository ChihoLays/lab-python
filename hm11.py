#Q1
from datetime import datetime
class Clock:
    def __init__(self):
        now = datetime.now()
        self.hh = int(now.strftime("%H"))
        self.mm = int(now.strftime("%M"))
        self.ss = int(now.strftime("%S"))
    def format_time(self):
        if self.ss >= 60:
            self.ss %= 60
            self.mm += 1
            if self.mm >= 60:
                self.mm %= 60
                self.hh += 1
                if self.hh > 23:
                    self.hh %= 24
    def run(self):
        self.ss += 1
        self.format_time()
    def setTime(self,h,m,s):
        self.hh = h
        self.mm = m
        self.ss = s
        self.format_time()
    def get_time(self):
        return f"{self.hh:02d}:{self.mm:02d}:{self.ss:02d}"

class AlarmClock(Clock):
    def __init__(self,ahour,amin,asec,aoorf):
        super().__init__()
        self.alarm_hh = ahour
        self.alarm_mm =amin
        self.alarm_ss = asec
        self.alarm_on_off = aoorf
    def setAlarmTime(self,h,m,s):
        self.alarm_hh = h
        self.alarm_mm = m
        self.alarm_ss = s
        if self.alarm_ss >= 60:
            self.alarm_ss %= 60
            self.alarm_mm += 1
            if self.alarm_mm >= 60:
                self.alarm_mm %= 60
                self.alarm_hh += 1
                if self.alarm_hh > 23:
                    self.alarm_hh %= 24
    def alarm_on(self):
        self.alarm_on_off = True
    def alarm_off(self):
        self.alarm_on_off = False
    def run(self):
        super().run()
        print(f"Current time: {super().get_time()}")
        if self.alarm_on_off == True and self.hh == self.alarm_hh and self.mm == self.alarm_mm and self.ss == self.alarm_ss:
            print(f"Alarmed\n{super().get_time()}")
            exit(0)
