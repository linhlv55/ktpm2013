from input import main
from sys import argv
import re
import itertools
import unittest
import inspect
# function check value of [a,b] in [c,d] ?
def CheckValue(a,b,c,d):
    check = 0
    if( a<c and c <b and b < d):
        check = 1
    if( a<c and c<d and d<b):
        check =1
    if ( c<a and a<d and d<b):
        check =1
    return check
#function check equivalence class?
def CheckEquivalenceClass(a):
    check =0
    i =0
    while i < len(a):
        if (i%2 ==0 and a[i]>a[i+1]):
            check =1
        i = i+1
    i = 0
    while i< len(a):
        j = 0
        while j < len(a):
            if(CheckValue(a[i],a[i+1],a[j],a[j+1]) ==1 and i != j):
                check = 1
            j = j+2
        i = i+2
    return check
#function get array from input
def GetArrayFromInput():
    global check_global
    #get docstring input to array
    arrayInput = main.__doc__
    arrayList =[]
    array =  arrayInput.split('\n')
    for i in array:
        if(array[0] == ''):
            del array[0]
        t = len(array) -1
        while t != 0:
            if(array[t] == ''):
                del array[t]
            t = t-1
    k = len(array)-1
    index =0
    check =0
    while index != k:
        number = re.findall(r'\d+', '%s' %(array[index]))
        number = map(int,number)
        if(CheckEquivalenceClass(number) == 1):
            check =1
        j=0
        arrayList.append(number)
        index = index +1
    leng = len(arrayList)
    check_global = check
    return arrayList
def GetArrayTest():
    arrayTest = []
    arrayList = GetArrayFromInput()
    i = 0
    while(i<len(arrayList)):
        j = 0
        num = []
        while(j< len(arrayList[i])):
              num.append((arrayList[i][j] + arrayList[i][j+1])/2)
              j = j+2
        arrayTest.append(num)
        i = i+1
    return arrayTest
def GetArrayTestCase():
    arrayTestCase = []
    arrayTest = GetArrayTest()
    i = 1
    st = ""
    lt = []
    lt.append(arrayTest[0])
    result = arrayTest[0]
    while i < len(arrayTest):
        lt.append(arrayTest[i])
        i = i+1
    arrayTestCase = list(itertools.product(*lt))
    arrlen  = len(arrayTestCase)
    return arrayTestCase
class TestSequense(unittest.TestCase):
    pass

def test_generator(a):
    def test(self):
        self.assertEqual(main(a),"test")
    return test
if __name__ == '__main__':
    arrayTestCase = GetArrayTestCase()
    if (check_global==1):
                raise Exception("wrong input")
    else:
        i=0
        for param in arrayTestCase:
            test_name = 'testName'+str(i)
            test = test_generator(param)
            setattr(TestSequense, test_name, test)
            i = i+1
        unittest.main()
