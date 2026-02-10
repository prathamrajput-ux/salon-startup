import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- CLOUD DATABASE CONFIGURATION ---
database_url = os.environ.get('DATABASE_URL', 'sqlite:///local.db')
if database_url and database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- DATABASE MODEL (UPDATED) ---
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    # Service column bada kar diya taaki multiple services aa sakein
    service = db.Column(db.String(500), nullable=False) 
    status = db.Column(db.String(20), default='Pending')

# Create Tables
with app.app_context():
    db.create_all()

# --- API ENDPOINTS ---

@app.route('/')
def home():
    return "Advanced Salon Backend is Live!"

# 1. Booking API (With Spam Check & Token)
@app.route('/book', methods=['POST'])
def book():
    data = request.json
    
    # SPAM CHECK: Kya is number se koi pending booking hai?
    existing_booking = Appointment.query.filter_by(phone=data['phone'], status='Pending').first()
    if existing_booking:
        return jsonify({"error": "⚠️ Aapki ek booking already line mein hai!"}), 400
    
    # MULTI-SERVICE HANDLING: List ko string mein badalna
    # Agar frontend se list aayi ['Haircut', 'Shave'] -> 'Haircut, Shave' ban jayega
    if isinstance(data['service'], list):
        services_str = ", ".join(data['service'])
    else:
        services_str = data['service']

    new_booking = Appointment(
        name=data['name'], 
        phone=data['phone'], 
        service=services_str
    )
    
    db.session.add(new_booking)
    db.session.commit()
    
    # Token ID wapas bhejo
    return jsonify({
        "message": "Booking Confirmed!", 
        "token": new_booking.id
    })

# 2. Status API (Current Token Logic)
@app.route('/status', methods=['GET'])
def get_status():
    pending_count = Appointment.query.filter_by(status='Pending').count()
    
    # Sabse pehla banda jo line mein hai (Current Token)
    current_person = Appointment.query.filter_by(status='Pending').order_by(Appointment.id).first()
    
    # Agar koi nahi hai toh 0, warna uska ID
    current_token_num = current_person.id if current_person else 0
    
    return jsonify({
        "people_ahead": pending_count,
        "wait_time": pending_count * 20, # 20 min per person average
        "current_token": current_token_num
    })

# 3. Admin Data (With Phone Number)
@app.route('/admin-data', methods=['GET'])
def admin_data():
    pending_list = Appointment.query.filter_by(status='Pending').all()
    output = []
    for p in pending_list:
        output.append({
            "id": p.id, 
            "name": p.name, 
            "service": p.service,
            "phone": p.phone # Phone number bhi bhej rahe hain taaki call kar sakein
        })
    return jsonify(output)

# 4. Mark Completed
@app.route('/complete/<int:id>', methods=['POST'])
def complete_task(id):
    appointment = Appointment.query.get(id)
    if appointment:
        appointment.status = 'Completed'
        db.session.commit()
        return jsonify({"message": "Done"})
    return jsonify({"error": "Not Found"}), 404

if __name__ == '__main__':
    app.run(debug=True)