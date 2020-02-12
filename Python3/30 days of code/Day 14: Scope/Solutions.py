class Difference:
    def __init__(self, a):
        self.__elements = a
##A class constructor that takes an array of integers as a parameter and saves it to the  elements instance variable.
    def computeDifference(self):
        min_element = min(self.__elements)
        max_element = max(self.__elements)
        self.maximumDifference = max_element - min_element
# A computeDifference method that finds the maximum absolute difference between any  2 numbers in  N and stores it in the  maximumDifference instance variable.
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
