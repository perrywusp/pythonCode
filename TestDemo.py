#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:perrywu 
@file: TestMarsCarDemo.py 
@time: 2019/04/28 
"""

from MarsCarDemo import MarsCarDemo


def test():

    # max x y and all mars car list
    max = {"xMax": 5, "yMax": 5}
    cars = []
    # ======================first mars car ======================
    pos1 = {"x": 1, "y": 2, "fc": "N", "rip": None}
    cmd1 = "L M L M L M L M M".split()
    print "================= first mars car position ====================="
    marsCar1 = MarsCarDemo()
    marsCar1.setXyMax(max)
    marsCar1.marsCarRunning(pos1, cmd1, cars)
    cars.append(marsCar1)
    print marsCar1.getMarsCarPos()

    print "================= second mars car position ===================="
    pos2 = {"x": 3, "y": 3, "fc": "E", "rip": None}
    cmd2 = "M M".split()
    marsCar2 = MarsCarDemo()
    marsCar2.setXyMax(max)
    marsCar2.marsCarRunning(pos2, cmd2, cars)
    cars.append(marsCar2)
    print marsCar2.getMarsCarPos()


if __name__ == "__main__":
    test()