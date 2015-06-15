# -*- coding: utf-8 -*-
# code for console Encoding difference. Dont' mind on it 
import sys
import imp
import random
imp.reload(sys)
try: sys.setdefaultencoding('UTF8')
except Exception as E: pass

try:
    import unittest2 as unittest
except ImportError:
    import unittest
from closedown import *

class CloseDownTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.closeDownChecker =  CloseDown('TESTER','SwWxqU+0TErBXy/9TVjIPEnI0VTUMMSQZtJf3Ed8q3I=')
        
    def test_getBalance(self):
        balance = self.closeDownChecker.getBalance()
        print(balance)
        self.assertGreaterEqual(balance,0,'잔액 0 이상.')

    def test_getUnitCost(self):
        unitCost = self.closeDownChecker.getUnitCost()
        print(unitCost)
        self.assertGreaterEqual(unitCost,0,"단가는 0 이상.")

    def test_checkCorpNum(self):
        corpState = self.closeDownChecker.checkCorpNum('1231212312')
        print(corpState.type)
        self.assertEqual(corpState.type,3,"면세였던가...")

    def test_checkCorpNums(self):
        corpStates = self.closeDownChecker.checkCorpNums(["1231212312","10000000"])
        print(corpStates[0])
        self.assertEqual(corpStates[0].type,3,"면세아닌가.")


if __name__ == '__main__':
    unittest.main()