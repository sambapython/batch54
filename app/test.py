import unittest
from main import fun, check_even
class FunTest(unittest.TestCase):
	def test_10_20(self):
		exp=30
		act = fun(10,20)
		self.assertEqual(exp,act,"test_10_20 failed")
	def test_10_str2(self):
		exp=None
		act = fun(10,"str2")
		self.assertEqual(exp,act,"test_10_str2 failed")
class EvenTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls): # will call before calling any test method
		print("login")
		cls.user="SAI"
	@classmethod
	def tearDownClass(cls): # will call after calling all test method
		print("logout")
		cls.user=None
	def setUp(self): # will call before calling every test case
		print("create resource")
	def tearDown(self): # will call after calling every test case
		print("delete resource")
	def test_10(self):
		#print("create resource")
		print(self.user)
		exp="EVEN"
		act=check_even(10)
		self.assertEqual(exp,act,"test_10 failed")
		#print("delete resource")
	def test_11(self):
		#print("create resource")
		print(self.user)
		exp="ODD"
		act=check_even(11)
		self.assertEqual(exp,act,"test_11 failed")
		print("delete resource")
	def test_str1(self):
		#print("create resource")
		exp=None
		print(self.user)
		act=check_even("str1")
		self.assertEqual(exp,act,"test_str1 failed")
		#print("delete resource")
	def test_empty(self):
		#print("create resource")
		print(self.user)
		exp="EVEN"
		act=check_even()
		self.assertEqual(exp,act,"test_str1 failed")
		#print("delete resource")

unittest.main()
