import unittest
import invoice
import datetime

class TestBuild(unittest.TestCase):

	def test_build_class(self):
		invoice.Build()
		self.assertEqual(invoice.customer_list[1], {'CustomerNo': 1123, 'Customer': 'Petrie Corp.', 'Address': 'Calgary, AB', 'Phone': '403-619-9773', 'Contact': 'Eva Lapp'} )
		self.assertEqual(invoice.invoice_list[1], {'InvoiceNo': 1, 'CustomerNo': 1123, 'Date': datetime.datetime(2019, 1, 1, 0, 0)})
		self.assertEqual(invoice.line_list[1], {'InvoiceNo': 1, 'ProductNo': 1, 'Units': 1})
		self.assertEqual(invoice.product_list[1], {'ProductNo': 1, 'Product': 'Item 1', 'UnitPrice': 45})
		

class TestCreate(unittest.TestCase):
	
	def test_create_invoice(self):
		invoice.Create.create_invoice(1)
	

if __name__ == "__main__":
		unittest.main()