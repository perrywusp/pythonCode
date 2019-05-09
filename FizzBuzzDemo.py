#!usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:perrywu 
@file: FizzBuzzDemo.py
@time: 2019/05/09 
"""


class FizzBuzzDemo:

    def __init__(self):
        self.fizz = "Fizz"
        self.buzz = "Buzz"

    def isFizz(self, num):
        return self.isDevidOrContained(num, 3)

    def isBuzz(self, num):
        return self.isDevidOrContained(num, 5)

    @staticmethod
    def isDevidOrContained(num, specialNum):
        numMap = map(int, str(num))
        return (num % specialNum == 0) or (specialNum in numMap)

    def say(self, num):
        result = ""
        if self.isFizz(num):
            result += self.fizz
        if self.isBuzz(num):
            result += self.buzz
        return num if (len(result) == 0) else result


if __name__ == "__main__":
    fizzBuzz = FizzBuzzDemo()
    for i in range(1, 100):
        print fizzBuzz.say(i)