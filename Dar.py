from asyncio.windows_events import NULL
import ctypes

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
        num = self.count
        if num == 0 and i == 0:
            num += 1
        for j in range(num):
            if j == i and i < self.count and self.count + 1 <= self.capacity:
                for x in range(self.count-1,i-1,-1):
                    self.array[x+1] = self.array[x]
                self.array[i] = itm
                self.count += 1
                break
            elif j == i and i < self.count and self.count + 1 > self.capacity:
                new_capacity = self.capacity + 1
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
                new_capacity = self.capacity + 1
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
                new_capacity = self.capacity + 1
                new_array = self.make_array(new_capacity)
                for x in range(self.count):
                    new_array[x] = self.array[x]
                self.array = new_array
                self.array[i] = itm
                self.count += 1
                self.capacity = new_capacity
                break
    def delete(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        for j in range(self.count):
            if j == i:
                for x in range(i,self.count):
                    if x+1 == self.count-1:
                        self.array[x] = self.array[x+1]
                        self.array[x+1] = None
                        break
                    self.array[x] = self.array[x+1]


da = DynArray()
da.insert(0,125453)
for i in range(10):
    da.append(i)
da.insert(1,125453)
da.insert(11,125453)
da.insert(5,125453)
da.insert(12,125453)
da.delete(0)
da.delete(0)
for i in range(10):
    print(da[i])