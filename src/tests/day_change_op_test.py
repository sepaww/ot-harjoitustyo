import unittest

import finance.Finance as F
import stocks.stockcreator as st_cr
import day_change_op.day_change_operator as op

class Ownedstocks():
    def __init__(self):
        self.owned=[0]*10
    
class Timer():
    def __init__(self):     
        self.day=1
class Test_DOP(unittest.TestCase):
    
    def setUp(self):
        self.time=Timer()
        self.time.day=4
        self.owned=Ownedstocks()
        self.finance=F.Finance(100, 60, 50)
        self.stocks=st_cr.create_stocks()
    def test_finance_update(self):
        op.finance_update(self.finance, self.time)
        self.assertEqual(self.finance.money, 110)
        self.assertEqual(self.finance.exp, 80)
        
    def test_finance_update_highday(self):
        self.time.day=10
        op.finance_update(self.finance, self.time)
        self.assertEqual(self.finance.exp, 100)
        
    def test_summary_zero(self):
        summ=op.summary(self.stocks, self.finance, self.owned)
        self.assertEqual(summ, 100)
    
    def test_summary_someowned(self):
        self.owned.owned[1]+=1
        summ=op.summary(self.stocks, self.finance, self.owned)
        curstock=self.stocks[-1]
    
        sumofmoney=0
        for i in range(len(curstock)):
            if self.owned.owned[i]>0:
                sumofmoney+=curstock[i][1]*self.owned.owned[i]
        sumofmoney+=self.finance.money
        self.assertEqual(summ, sumofmoney)
