import sys

from DynamicArray import DynamicArray

array = DynamicArray()

try:
    array.append(40)
    array.append(41)
    array.append(44)
    array.insertAt(3, 45)
    array.append(46)

    print("The Array is: ", array)
except:
    print('Exception')
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2])
