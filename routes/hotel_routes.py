from flask import request, jsonify
from models.hotel import Hotel
import logging

def hotel_routes(app, db):
    @app.route('/create_hotel', methods=['POST'])
    def create_hotel():
        try:
            data = request.json
            expected_fields = ["hotelName", "price", "img"]

            # Check if required fields are missing
            missing_fields = [
                field for field in expected_fields if field not in data]
            if missing_fields:
                return jsonify({"message": f"Missing required fields: {', '.join(missing_fields)}"}), 400
            

            new_hotel = Hotel(
                hotelName=data['hotelName'],
                price=data['price'],
                img=data['img']
            )
            db.session.add(new_hotel)
            db.session.commit()
            return jsonify({'message': 'Hotel created successfully'}), 201
        except Exception as e:
            logging.error(f"Error creating hotel: {e}")
            return jsonify({"message": f"An error occurred: {e}"}), 500
        
    @app.route('/get_hotels', methods=['GET'])
    def get_hotels():
        try:
            hotels = Hotel.query.all()

            hotel_list = []
            for hotel in hotels:
                hotel_dict = {
                    "hotelName": hotel.hotelName,
                    "price": hotel.price,
                    "img": hotel.img
                }
                hotel_list.append(hotel_dict)
            
            return jsonify(hotel_list), 200
        except Exception as e:
            logging.error(f"Error getting hotels: {e}")
            return jsonify({"message": f"An error occurred: {e}"}), 500
        

    @app.route('/get_hotels/<int:hotel_id>', methods=['GET'])
    def get_hotel(hotel_id):
        try:
            hotel = Hotel.query.filter_by(id=hotel_id).first()
            if not hotel:
                return jsonify({"message": "Hotel not found"}), 404

            hotel_dict = {
                "hotelName": hotel.hotelName,
                "price": hotel.price,
                "img": hotel.img
            }
            
            return jsonify(hotel_dict), 200
        except Exception as e:
            logging.error(f"Error getting hotel: {e}")
            return jsonify({"message": f"An error occurred: {e}"}), 500
        
    @app.route('/delete_hotel/<int:hotel_id>', methods=['DELETE'])
    def delete_hotel(hotel_id):
        try:
            hotel = Hotel.query.filter_by(id=hotel_id).first()
            if not hotel:
                return jsonify({"message": "Hotel not found"}), 404

            db.session.delete(hotel)
            db.session.commit()
            
            return jsonify({"message": "Hotel deleted successfully"}), 200
        except Exception as e:
            logging.error(f"Error deleting hotel: {e}")
            return jsonify({"message": f"An error occurred: {e}"}), 500
        
    @app.route('/edit_hotel/<int:hotel_id>', methods=['PATCH'])
    def edit_hotel(hotel_id):
        try:
            hotel = Hotel.query.filter_by(id=hotel_id).first()
            if not hotel:
                return jsonify({"message": "Hotel not found"}), 404
            data = request.json
            
            # Extract patch_data, id, and data from the JSON payload
            patch_data = data.get("patch_data", [])
            if not patch_data:
                return jsonify({"message": "No data provided for update"}), 400
            
            # data = request.json
            # hotelName=data['hotelName']
            # price=data['price']
            # img=data['img']

            # hotel.hotelName = hotelName
            # db.session.commit()
            for patch in patch_data:
                target = patch.get("target")
                data = patch.get("data")

                # Check if the target attribute exists in the Hotel model
                if hasattr(Hotel, target):
                    # Use setattr to dynamically set the attribute
                    setattr(hotel, target, data)
                else:
                    # Handle the case where the target attribute doesn't exist
                    logging.warning(
                        f"Attribute '{target}' does not exist in the Hotel model.")
                    
            db.session.commit()
            
            return jsonify({"message": "Hotel updated successfully"}), 200
        except Exception as e:
            logging.error(f"Error updating hotel: {e}")
            return jsonify({"message": f"An error occurred: {e}"}), 500
        
    @app.route('/hotel/guests/<int:hotel_id>', methods=['GET'])
    def hotel_guests(hotel_id):
        try:
            hotel = Hotel.query.filter_by(id=hotel_id).first()
            guest_list = []
            for guest in hotel.guests:
                guest_dict = {
                    "id": guest.id,
                    "fisrtName": guest.firstName,
                    "secondName": guest.secondName,
                    "email": guest.email,
                    "mobile": guest.mobile
                }
                guest_list.append(guest_dict)   
            return jsonify(guest_list), 200
        except Exception as e:
            logging.error(f"Error getting guests: {e}")
            return jsonify({"message": f"An error occurred: {e}"}), 500