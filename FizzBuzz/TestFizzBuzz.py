#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:perrywu 
@file: TestFizzBuzz.py
@time: 2019/05/09 
"""

import unittest
from FizzBuzzDemo import *


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzBuzz = FizzBuzzDemo()

    def tearDown(self):
        pass

    def testSay(self):
        self.assertTrue(self.fizzBuzz.say(3) == "Fizz")
        self.assertTrue(self.fizzBuzz.say(5) == "Buzz")
        self.assertTrue(self.fizzBuzz.say(51) == "FizzBuzz")
        self.assertTrue(self.fizzBuzz.say(61) == 61)

if __name__ == "__main__":
    unittest.main()