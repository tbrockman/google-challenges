# You are given a list of numbers. When you reach the end of the list you will
# come back to the beginning of the list (a circular list). Write the most
# efficient algorithm to find the minimum # in this list. Find any given # in
# the list. The numbers in the list are always increasing but you don’t know
# where the circular list begins, ie: 38, 40, 55, 89, 6, 13, 20, 23, 36.

# The following code assumes:
# - the list is NOT a linked list, and can still be randomly accessed
# - the circular property can be implemented using the modulo operator
# - the input is increasing up until the point where it wraps around
#   i.e, there is an offset which will turn it into a regular list
# Solution should be O(logn) to find the offset (I think?)
# O(logn) to find arbitrary elements afterwards

import math
import sys

class CircularList:

    def __init__(self, list):
        self.list = list
        self.length = len(self.list)
        self.offset = self.find_offset() # the min is also at this index

    def __getitem__(self, i):
        if (self.offset != None):
            return self.list[(i + self.offset) % self.length]

    def find_offset(self):
        # start at the last element of the list
        midpoint = self.length - 1
        min = math.inf
        start = 0
        end = midpoint
        # no elements, one element, already sorted
        if (midpoint == -1):
            return None

        elif (midpoint == 0 or self.list[start] < self.list[end]):
            return 0
        # otherwise len(list) >= 2
        else:
            # if len(list) == 2, fails conditional and returns midpoint
            while (midpoint > 1 and start != end):
                # found the midpoint
                if (self.list[midpoint] < self.list[midpoint-1]):
                    return midpoint
                # otherwise take a step based on the minimum value we've seen
                else:

                    if (self.list[midpoint] > min):
                        start = midpoint
                        midpoint += (end - midpoint) // 2

                    elif (self.list[midpoint] <= min):
                        min = self.list[midpoint]
                        end = midpoint
                        midpoint -= (midpoint - start) // 2

            return midpoint

    def get_min(self):

        if (self.offset != None):
            return self.list[self.offset]
        else:
            return None

    def find(self, target):
        # overloaded array indexing with an awareness of the offset
        # now just use regular binary search
        left = 0
        right = self.length - 1

        while (left <= right):
            mid = (left + right) // 2

            if (self[mid] < target):
                left = mid + 1
            elif (self[mid] > target):
                right = mid - 1
            else:
                return mid

        return -1

def string_list_to_int(input):
    ints = [int(num) for num in input.split(" ")]
    return ints

if __name__ == "__main__":
    string_list = input("Enter a space-separated circular list of integers: ")
    ints = string_list_to_int(string_list)
    circular_list = CircularList(ints)
    print("List minimum:", circular_list.get_min())

    while (True):
        target = input("Find element within list: ")

        if (target == ""):
            break
        else:
            # NOTE:
            # This returns the index of the element as if the array were
            # shifted until the minimal element in the list resides at index 0
            index = circular_list.find(int(target))
            print(index)
