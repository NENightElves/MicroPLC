from machine import Pin
import time


class C_74HC595:

    def __init__(self, SER, SCK, RCK, amount=1, delay=10):
        self.SER = Pin(SER, Pin.OUT)
        self.SCK = Pin(SCK, Pin.OUT)
        self.RCK = Pin(RCK, Pin.OUT)
        self.amount = amount
        self.datalength = amount*8
        self.delay = delay

    def write(self, l: list):
        if len(l) > self.datalength:
            raise Exception('length error')
        for _ in l:
            if _ != 0 or _ != 1:
                raise Exception('value error')
        for _ in l:
            self.SCK.off()
            time.sleep_us(self.delay)
            self.SER.value(_)
            time.sleep_us(self.delay)
            self.SCK.on()
            time.sleep_us(self.delay)
        for _ in range(0, self.datalength-len(l)):
            self.SCK.off()
            time.sleep_us(self.delay)
            self.SER.value(0)
            time.sleep_us(self.delay)
            self.SCK.on()
            time.sleep_us(self.delay)
        self.RCK.off()
        time.sleep_us(self.delay)
        self.RCK.on()


class C_74HC165:

    def __init__(self, Q7, CP, PL, amount=1, delay=10):
        self.Q7 = Pin(Q7, Pin.IN)
        self.CP = Pin(CP, Pin.OUT)
        self.PL = Pin(PL, Pin.OUT)
        self.amount = amount
        self.datalength = amount*8
        self.delay = delay

    def read(self) -> list:
        l = []
        self.CP.on()
        time.sleep_us(self.delay)
        self.PL.off()
        time.sleep_us(self.delay)
        self.PL.on()
        time.sleep_us(self.delay)
        for _ in range(0, self.datalength):
            self.CP.off()
            time.sleep_us(self.delay)
            l.append(self.Q7.value())
            time.sleep_us(self.delay)
            self.CP.on()
            time.sleep_us(self.delay)
        return l
