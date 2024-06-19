from flask import request, jsonify
from models.bookings import Booking
from models.guest import Guest
import logging
from datetime import datetime

def user_routes(app, db):
    @app.route('/guest/booked_hotels/<int:guest_id>', methods=['GET'])
    def booked_hotels(guest_id):
        try:
            guest = Guest.query.filter_by(id=guest_id).first()
            hotel_list = []
            for hotel in guest.hotels:
                hotel_dict = {
                    "id": hotel.id,
                    "hotelName": hotel.hotelName,
                    "price": hotel.price,
                    "img": hotel.img
                }
                hotel_list.append(hotel_dict)   
            return jsonify(hotel_list), 200
        except Exception as e:
            logging.error(f"Error getting booked hotel: {e}")
            return jsonify({"message": f"An error occurred: {e}"}), 500