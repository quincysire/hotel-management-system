from models.dbconfig import db

class Hotel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotelName = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    img = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Hotel {self.hotelName}>'