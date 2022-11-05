noOfInputs = int(input("Enter num of elements"))
arr = []

for i in range(noOfInputs):
    a = int(input())
    arr.append(a)

findingNo = int(input("Enter the num to find"))

def findTheNumber(arr, findingNo):
    for i in arr:
        if(i == findingNo):
            return (i)

findTheNumber(arr,findingNo)

import unittest

class TestStringMethods(unittest.TestCase):

    def test_finding(self):
        a = findTheNumber([1,2,3],3)
        self.assertEqual(a, 3)

if __name__ == '__main__':
    unittest.main()