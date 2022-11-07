noOfInputs = int(input("Enter num of elements"))
arr = []
newArr = []

for i in range(noOfInputs):
    a = int(input('Enter the element'))
    arr.append(a)

findingNo = int(input("Enter the num to find"))

def findTheNumber(arr, findingNo):
    arr = [1,3,5,7]
    arr.sort()
    for i in range(len(arr)+1):
        if(arr[i] == findingNo):
            return arr[i]
        else:
            newArr.append(abs(arr[i]-findingNo))
            idx = newArr.index(min(newArr))
            return arr[idx]

            
    



findTheNumber(arr,findingNo)

import unittest

class TestStringMethods(unittest.TestCase):

    def test_finding(self):
        c = findTheNumber([1,2,3],2)
        self.assertEqual(c, 2)

    def test_notFinding(self):
        d = findTheNumber([1,2,5],3)
        self.assertEqual(d, 2)


if __name__ == '__main__':
    unittest.main()
