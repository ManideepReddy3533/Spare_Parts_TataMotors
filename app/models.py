from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class AutoSparePart(db.Model):
    __tablename__ = 'auto_spare_parts'

    id = db.Column(db.Integer, primary_key=True)
    part_name = db.Column(db.String(100))
    manufacturer_name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    identification_no = db.Column(db.String(100), unique=True)
    warranty = db.Column(db.String(50))
    manufactured_date = db.Column(db.Date)
    part_weight = db.Column(db.Float)

print("db success")

class Dealer(db.Model):
    __tablename__ = 'dealer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))

class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    contact_info = db.Column(db.String(100))
    address = db.Column(db.String(200))

class Sale(db.Model):
    __tablename__ = 'sale'

    id = db.Column(db.Integer, primary_key=True)
    dealer_id = db.Column(db.Integer, db.ForeignKey('dealer.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    part_id = db.Column(db.Integer, db.ForeignKey('auto_spare_parts.id'))  # ✅ fixed
    sale_date = db.Column(db.Date)
    quantity = db.Column(db.Integer)

print("models.py__ success")
