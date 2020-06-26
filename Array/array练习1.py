"""
:Author:  Mr.Fang
:Create:  2020/6/19 10:48
:Github:  https://github.com/WeaponMaster
Copyright (c) 2020, Mr.Fang Group All Rights Reserved.
"""

class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def insert(self, index, element):

        if index < 0 or index > len(self.array):
            raise Exception("数组越界")
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def output(self):
        for i in range(self.size):
            print(self.array[i], end='<-')


if __name__ == '__main__':
    array = Array(3)
    array.insert(0, 0)
    array.insert(1, 1)
    array.insert(2, 2)
    array.insert(3, 3)
    array.insert(4, 4)
    array.insert(5, 5)
    array.output()
