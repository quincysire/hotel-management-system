from models.dbconfig import db
from models.bookings import Booking 

class Guest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    secondName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    mobile = db.Column(db.String(15))
    role = db.Column(db.String(20), default='guest', nullable=False)

    bookings = db.relationship('Booking', back_populates='guest')
    hotels = db.relationship('Hotel', secondary='booking', back_populates='guests')

    def __repr__(self):
        return f'<Guest {self.firstName} {self.secondName}>'