
from models.tysql_models import *
from explore import app

db.session.query(Customers).all()