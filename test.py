import pytest
from sumEvenNumber import SumEvenNum

def test_sumofevennumber():
	sum1=SumEvenNum(1,20)
	assert ( sum1.sumEvenNum()==110)
	sum2=SumEvenNum(30,60)
	assert (sum2.sumEvenNum() == 720)
