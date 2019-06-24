from project import db, Customer

db.create_all()

Streamside = Customer('Streamside Welding and Fabrication', 'Jeff Lapp', 4036199773)
Grizzly = Customer('Grizzly Welding Services', 'Chris Sebolsky', 4039901234)
Freestone = Customer('Freestone Welding Ltd', 'Daniel Lachance', 4036671298 )

print(Grizzly.id)

db.session.add_all([Streamside,Grizzly,Freestone])

db.session.commit()

print(Grizzly.id)