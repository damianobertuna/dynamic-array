import sys

from DynamicArray import DynamicArray

array = DynamicArray()

try:
    array.append(40)
    array.append(41)
    array.append(44)
    array.append(48)
    array.insertAt(3, 45)
    array.append(46)
    array.insertAt(3, 50)
    array.insertAt(5, 49)
    array.insertAt(7, 51)
    print("The Array is: ", array)
    array.delete()
    print("The Array now is: ", array)
    array.removeAt(0)
    print("The Array now is: ", array)
except:
    print('Exception')
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])
