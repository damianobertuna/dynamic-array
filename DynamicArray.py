import ctypes


class DynamicArray(object):
    def __init__(self):
        self.actualNumElement = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.actualNumElement

    def __getItem__(self, index):
        if not 0 <= index < self.actualNumElement:
            raise Exception('Index not found')

        return self.A[index]

    def append(self, element):
        if self.actualNumElement == self.capacity:
            self.__resize(2 * self.capacity)

        self.A[self.actualNumElement] = element
        self.actualNumElement += 1

    def insertAt(self, index, elem):
        if index < 0 or index > self.actualNumElement:
            raise Exception('Index not permitted')

        if self.actualNumElement == self.capacity:
            self.__resize(2 * self.capacity)

        for i in range(self.actualNumElement-1, index-1, -1):
            self.A[i+1] = self.A[i]

        self.A[index] = elem
        self.actualNumElement += 1

    def __resize(self, newCapacity):
        B = self.make_array(newCapacity)
        for index in range(self.actualNumElement):
            B[index] = self.A[index]

        self.A = B
        self.capacity = newCapacity

    def make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    def __str__(self):
        arrayString = '['
        for i in range(0, self.actualNumElement):
            arrayString += str(self.A[i]) + ", "
        return arrayString.rstrip(', ') + ']'