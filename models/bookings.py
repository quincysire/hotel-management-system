from models.dbconfig import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey(
        'guest.id'), nullable=False)
    hotel_id = db.Column(
        db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    check_in = db.Column(db.DateTime)
    check_out = db.Column(db.DateTime)

    
    # Relationships to Guest and Hotel
    guest = db.relationship('Guest', back_populates='bookings')
    hotel = db.relationship('Hotel', back_populates='bookings')
