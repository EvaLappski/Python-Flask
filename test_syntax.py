import unittest
import syntax

class TestSyntax(unittest.TestCase):

	def test_add(self):
		result = syntax.add(1, 1)
		self.assertEqual(result, 2)
		self.assertEqual(syntax.add(0,0),0)
		self.assertEqual(syntax.add(-1,1),0)
		self.assertEqual(syntax.add(1,-5),-4)
		self.assertEqual(syntax.add(-1,-5),-6)

	def test_sub(self):
		self.assertEqual(syntax.sub(1,1),0)
		self.assertEqual(syntax.sub(10,11),-1)
		self.assertEqual(syntax.sub(11,10),1)
		self.assertEqual(syntax.sub(-1,-1),0)
		self.assertEqual(syntax.sub(-1,1),-2)

	def test_multiply(self):
		self.assertEqual(syntax.multiply(2,5), 10)
		self.assertEqual(syntax.multiply(2,-5), -10)
		self.assertEqual(syntax.multiply(-2,5), -10)
		self.assertEqual(syntax.multiply(-2,-5), 10)

	def test_divide(self):
		self.assertEqual(syntax.divide(100,25), 4)
		self.assertEqual(syntax.divide(100,-10), -10)
		self.assertEqual(syntax.divide(-100,-10), 10)
		self.assertRaises(ValueError, syntax.divide, 10, 0)

	def test_email(self):
		self.assertEqual(syntax.email('Eva','Lapp'), 'eva.lapp@evolveu.ca')
		self.assertEqual(syntax.email('Larry','Shumlich'), 'larry.shumlich@evolveu.ca')
		
	def test_tax_calc(self):
			self.assertEqual(syntax.tax_calc(11000), 0)
			self.assertEqual(syntax.tax_calc(47000), 7050)
			self.assertEqual(syntax.tax_calc(50000), 7630.85)
			self.assertEqual(syntax.tax_calc(100000), 18141.66)
			self.assertEqual(syntax.tax_calc(150000), 31211.57)
			self.assertEqual(syntax.tax_calc(250000), 61796.57)
		


		