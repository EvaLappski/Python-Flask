import openpyxl
import sys
import glob
import xlrd
import xlsxwriter


file_names = []

class Mergedata():

	@staticmethod
	def merge():

		file_names_temp = []
		temp_word = '~$'
		master_file = "master_file"
		for file in glob.glob('*.xlsx'):
			file_names_temp.append(file)
		for file in file_names_temp:
			if (temp_word not in file) and (master_file not in file):
				file_names.append(file)

		rows = []
		rows2 = []
		rows3 = []
		rows4 =[]

		for file in file_names:
			try:
				workbook_to_read = xlrd.open_workbook(file)
				customers_sheet_to_read = workbook_to_read.sheet_by_index(0)
				invoices_sheet_to_read = workbook_to_read.sheet_by_index(1)
				lineitems_sheet_to_read = workbook_to_read.sheet_by_index(2)
				products_sheet_to_read = workbook_to_read.sheet_by_index(3)
				for x in range(customers_sheet_to_read.nrows - 1):
					a_column_value = customers_sheet_to_read.cell_value(x + 1, 0) 
					b_column_value = customers_sheet_to_read.cell_value(x + 1, 1) 
					c_column_value = customers_sheet_to_read.cell_value(x + 1, 2) 
					d_column_value = customers_sheet_to_read.cell_value(x + 1, 3) 
					e_column_value = customers_sheet_to_read.cell_value(x + 1, 4) 
					row = [a_column_value, b_column_value, c_column_value, d_column_value, e_column_value]
					rows.append(row)
				for y in range(invoices_sheet_to_read.nrows - 1):
					a_column_value = invoices_sheet_to_read.cell_value(y + 1, 0) 
					b_column_value = invoices_sheet_to_read.cell_value(y + 1, 1) 
					c_column_value = invoices_sheet_to_read.cell_value(y + 1, 2) 
					row = [a_column_value, b_column_value, c_column_value]
					rows2.append(row)
					# print(rows2)
				for z in range(lineitems_sheet_to_read.nrows - 1):
					a_column_value = lineitems_sheet_to_read.cell_value(z + 1, 0) 
					b_column_value = lineitems_sheet_to_read.cell_value(z + 1, 1) 
					c_column_value = lineitems_sheet_to_read.cell_value(z + 1, 2) 
					row = [a_column_value, b_column_value, c_column_value]
					rows3.append(row)
				for q in range(products_sheet_to_read.nrows - 1):
					a_column_value = products_sheet_to_read.cell_value(q + 1, 0) 
					b_column_value = products_sheet_to_read.cell_value(q + 1, 1) 
					c_column_value = products_sheet_to_read.cell_value(q + 1, 2) 
					row = [a_column_value, b_column_value, c_column_value]
					rows4.append(row)
			except:
				print("ERROR : UNABLE TO OPEN FILE " + file)

				sys.exit(0)

				
			workbook_to_write = xlsxwriter.Workbook('master_file.' + "xlsx")

			customers_sheet_to_merge = workbook_to_write.add_worksheet('Customers')
			invoices_sheet_to_merge = workbook_to_write.add_worksheet('Invoices')
			lineitems_sheet_to_merge = workbook_to_write.add_worksheet('Line Items')
			products_sheet_to_merge = workbook_to_write.add_worksheet('Products')

			customers_sheet_to_merge.write('A1', 'Customer Number')
			customers_sheet_to_merge.write('B1', 'Customer Name')
			customers_sheet_to_merge.write('C1', 'Address')
			customers_sheet_to_merge.write('D1', 'Phone')
			customers_sheet_to_merge.write('E1', 'Contact')

			invoices_sheet_to_merge.write('A1', 'Invoice Number')
			invoices_sheet_to_merge.write('B1', 'Customer Number')
			invoices_sheet_to_merge.write('C1', 'Date')

			lineitems_sheet_to_merge.write('A1', 'Invoice Number')
			lineitems_sheet_to_merge.write('B1', 'Product Number')
			lineitems_sheet_to_merge.write('C1', 'Units')

			products_sheet_to_merge.write("A1", 'Product Number')
			products_sheet_to_merge.write("A1", 'Product Name')
			products_sheet_to_merge.write("A1", 'Unit Cost')

			count = 1

			for row in rows:
				for x in range(0, 5):
					customers_sheet_to_merge.write_string(count, x, str(row[x]))
				count = count +1

			count2 = 1
			for row in rows2:
				for y in range(0, 3):
					invoices_sheet_to_merge.write_string(count2, y, str(row[y]))
				count2 = count2 +1

			count3 = 1
			for row in rows3:
				for z in range(0, 3):
					lineitems_sheet_to_merge.write_string(count3, z, str(row[z]))
				count3 = count3 +1

			count4 = 1
			for row in rows4:
				for q in range(0, 3):
					products_sheet_to_merge.write_string(count4, q, str(row[q]))
				count4 = count4 +1
				
			workbook_to_write.close()

Mergedata.merge()
# Mergedata.read_customers()
# # Mergedata.read_invoices()
# Mergedata.write()