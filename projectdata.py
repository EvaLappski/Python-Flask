from project import db, Customer, Invoice
import datetime

db.create_all()

Streamside = Customer('Streamside Welding and Fabrication', 'Jeff Lapp', 4036199773)
Grizzly = Customer('Grizzly Welding Services', 'Chris Sebolsky', 4039901234)
Freestone = Customer('Freestone Welding Ltd', 'Daniel Lachance', 4036671298 )

print(Grizzly.id)

db.session.add_all([Streamside,Grizzly,Freestone])

db.session.commit()

print(Grizzly.id)

db.create_all()
one = Invoice(1,datetime.datetime(2006-01-01))
two = Invoice(2,datetime.datetime(2009-06-01))

db.session.add_all([one, two])
db.session.commit()

print("test",one.date)