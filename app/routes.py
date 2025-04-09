from flask import Blueprint, request, jsonify
from .models import db, AutoSparePart, Dealer, Customer, Sale
from datetime import datetime



main = Blueprint('main', __name__)
@main.route('/')
def home():
    return "✅ Flask App is Running Successfully with MySQL!"

@main.route('/add_spare_part', methods=['POST'])
def add_spare_part():
    data = request.get_json()
    part = AutoSparePart( 
        part_name=data['part_name'],
        manufacturer_name=data['manufacturer_name'],
        location=data['location'],
        identification_no=data['identification_no'],
        warranty=data['warranty'],
        manufactured_date=datetime.strptime(data['manufactured_date'], "%Y-%m-%d"),
        part_weight=data['part_weight']
    )
    
    db.session.add(part)
    db.session.commit()
    return jsonify({"message": "Spare part added"}), 201

print("success")