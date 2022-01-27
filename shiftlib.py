from machine import Pin
import time


class C_74HC595:

    def __init__(self, SER, SCK, RCK, amount=1):
        self.SER = Pin(SER, Pin.OUT)
        self.SCK = Pin(SCK, Pin.OUT)
        self.RCK = Pin(RCK, Pin.OUT)
        self.amount = amount
        self.datalength = amount*8

    def write(self, l: list):
        if len(l) > self.datalength:
            raise Exception('length error')
        for _ in l:
            if _ != 0 or _ != 1:
                raise Exception('value error')
        for _ in l:
            self.SCK.off()
            self.SER.value(_)
            self.SCK.on()
        for _ in range(0, self.datalength-len(l)):
            self.SCK.off()
            self.SER.value(0)
            self.SCK.on()


class C_74HC165:

    def __init__(self, Q7, CP, PL, amount=1):
        self.Q7 = Pin(Q7, Pin.IN)
        self.CP = Pin(CP, Pin.OUT)
        self.PL = Pin(PL, Pin.OUT)
        self.amount = amount
        self.datalength = amount*8

    def read(self) -> list:
        l = []
        self.CP.on()
        self.PL.off()
        self.PL.on()
        for _ in range(0, self.datalength):
            self.CP.off()
            l.append(self.Q7.value())
            self.CP.on()
        return l
