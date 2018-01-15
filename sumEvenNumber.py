#!/usr/bin/python

class SumEvenNum:

	def __init__(self,a,b):
		if (a % 2 == 0):
			self.a=a
		else:
			self.a=a+1					
		self.b=b
		self.sum=0
		
	def sumEvenNum(self):
		SumEvenNum.sum = sum(range(self.a,self.b+1,2))
		print "sum of even numbers for:", self.a, self.b,"=", SumEvenNum.sum	
		return SumEvenNum.sum

