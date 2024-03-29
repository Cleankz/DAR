from asyncio.windows_events import NULL
import ctypes
import random

class DynArray:

    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i == 0:
            return self.array[i]
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        if i < 0 or i > self.count:
            raise IndexError('Index is out of bounds')
        for j in range(self.count):
            if j == i and i < self.count and self.count + 1 <= self.capacity:
                for x in range(self.count-1,i-1,-1):
                    self.array[x+1] = self.array[x]
                self.array[i] = itm
                self.count += 1
                break
            elif j == i and i < self.count and self.count + 1 > self.capacity:
                new_capacity = self.capacity * 2
                new_array = self.make_array(new_capacity)
                for x in range(self.count):
                    new_array[x] = self.array[x]
                self.array = new_array
                for x in range(self.count-1,i-1,-1):
                    self.array[x+1] = self.array[x]
                self.array[i] = itm
                self.count += 1
                self.capacity = new_capacity
                break
            elif j == i and i == self.count and self.count + 1 < self.capacity:
                self.array[i] = itm
                self.count += 1
                break
            elif j == i and i == self.count and self.count + 1 > self.capacity:
                new_capacity = self.capacity * 2
                new_array = self.make_array(new_capacity)
                for x in range(self.count):
                    new_array[x] = self.array[x]
                self.array = new_array
                self.array[i] = itm
                self.count += 1
                self.capacity = new_capacity
                break
            elif i == self.count and self.count + 1 <= self.capacity:
                self.array[i] = itm
                self.count += 1
                break
            elif i == self.count and self.count + 1 > self.capacity:
                new_capacity = self.capacity * 2
                new_array = self.make_array(new_capacity)
                for x in range(self.count):
                    new_array[x] = self.array[x]
                self.array = new_array
                self.array[i] = itm
                self.count += 1
                self.capacity = new_capacity
                break
        if  i == 0 and self.count == 0:
            self.append(itm)

    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for j in range(self.count):
            if i == self.count - 1:
                self.array[i] = None
                self.count -=1
                break
            if j == i:
                for x in range(i,self.count):
                    if x+1 == self.count-1:
                        self.array[x] = self.array[x+1]
                        self.array[x+1] = None
                        break
                    self.array[x] = self.array[x+1]
                self.count -=1
                break
        if self.count < int(self.capacity // 2):
            new_capacity = int(self.capacity // 1.5)
            if new_capacity < 16:
                new_capacity = 16
            self.resize(int(new_capacity))