# Bubble Sort
import time

class Solution(object):
    def bubble_sort(self, nums):
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums


# test the correctness
obj = Solution()
print(obj.bubble_sort([6,53,32,76,223,771,0,1]))

# generate a list of n items and show time consumption
def time_consume(n):
    a = []
    for i in range(n):
        a.append(i)
    # to get the current time in milli seconds
    start = int(round(time.time() * 1000))
    obj.bubble_sort(a)
    end = int(round(time.time() * 1000))
    ms = end - start
    return ms

print("bubble sort takes {} ms to sort 10 items.".format(time_consume(10)))
print("bubble sort takes {} ms to sort 100 items.".format(time_consume(100)))
print("bubble sort takes {} ms to sort 1000 items.".format(time_consume(1000)))
print("bubble sort takes {} ms to sort 10000 items.".format(time_consume(10000)))