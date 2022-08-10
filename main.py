import sys

from DynamicArray import DynamicArray

array = DynamicArray()

try:
    array.append(40)
    array.append(41)
    array.append(44)
    array.append(48)
    print(array)
    array.insertAt(3, 45)
    array.append(46)
    array.insertAt(3, 50)
    print(array)
    array.insertAt(5, 49)
    print(array)
    array.insertAt(7, 51)
    print(array)
    array.delete()
    print(array)
    array.removeAt(4)
    print(array)
except:
    print('Exception')
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])
