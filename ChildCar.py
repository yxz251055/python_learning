from Car import *
class ChildCar(Car):

    def __init__(self,name,age):
        super().__init__(name,age)
        self.sex = bike()

    def printmsg(self):
        print('============我改写的=================')

my = ChildCar('byd',13)
my.printmsg()
from bick import *

my.sex.printa()