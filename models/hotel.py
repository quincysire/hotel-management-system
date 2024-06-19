from models.dbconfig import db
from models.bookings import Booking

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotelName = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    img = db.Column(db.String(), nullable=False)

    # relationships
    bookings = db.relationship('Booking', back_populates='hotel')
    guests = db.relationship('Guest', secondary='booking', back_populates='hotels')

    def __repr__(self):
        return f'<Hotel {self.hotelName}>'