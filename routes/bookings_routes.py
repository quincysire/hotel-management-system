from flask import request, jsonify
from models.bookings import Booking
import logging
from datetime import datetime

def bookings_routes(app, db):
    @app.route('/book_hotel/<int:hotel_id>', methods=['POST'])
    def book_hotel(hotel_id):
        try:
            data = request.json
            expected_fields = ["guest_id", "check_in", "check_out"]

            # Check if required fields are missing
            missing_fields = [
                field for field in expected_fields if field not in data]
            if missing_fields:
                return jsonify({"message": f"Missing required fields: {', '.join(missing_fields)}"}), 400
            

            new_booking = Booking(
                hotel_id=hotel_id,
                guest_id=data['guest_id'],
                check_in=datetime.strptime(data['check_in'], '%d-%m-%Y'),
                check_out=datetime.strptime(data['check_out'], '%d-%m-%Y')
            )
            db.session.add(new_booking)
            db.session.commit()
            return jsonify({'message': 'Hotel booked successfully'}), 201
        except Exception as e:
            logging.error(f"Error booking hotel: {e}")
            return jsonify({"message": f"An error occurred: {e}"}), 500