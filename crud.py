from project import db, Customer

# CREATE
new_customer = Customer('Strathcona Mechanical', 'Robert Dyer', 4034456782)
db.session.add(new_customer)
db.session.commit()

#READ
all_customers = Customer.query.all()
# print(all_customers)
customer_one = Customer.query.get(1)
# print(customer_one.customer_name)

#FILTER
# search = Customer.query.filter_by(contact='Chris Sebolsky')
# print(search.all())

#UPDATE
edit = Customer.query.get(1)
edit.phone = 4034404444
db.session.add(edit)
db.session.commit()
# print(all_customers)

# DELETE
# delete_customer = Customer.query.get(1)
# db.session.delete(delete_customer)
# db.session.commit()
# print("test",all_customers)





