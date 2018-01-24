
from models.tysql_models import *
from explore import app

db.session.query(Customers).all()

prod = db.session.query(Products).first()
prod.vendor

vend = db.session.query(Vendors).first()
vend.products.all()



