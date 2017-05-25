# provides getsizeof() function
import sys

data = []
for k in range(100):
    a = len(data)               # number of elements
    b = sys.getsizeof(data)     # actual sizes in bytes
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    if k % 4 == 0:
        print('-'*50)
    data.append(None)           # increase size by None


