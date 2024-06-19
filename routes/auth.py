from flask import request, jsonify
import logging
from models.guest import Guest
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

def auth(app, db):
    @app.route('/register', methods=['POST'])
    def register():
        try:
            data = request.json
            expected_fields = ["firstName", "secondName", "email", "password", "mobile"]

            # Check if required fields are missing
            missing_fields = [
                field for field in expected_fields if field not in data]
            if missing_fields:
                return jsonify({"message": f"Missing required fields: {', '.join(missing_fields)}"}), 400
            

            new_guest = Guest(
                firstName=data['firstName'],
                secondName=data['secondName'],
                email=data['email'],
                password=generate_password_hash(data["password"]),  # hash the password
                mobile=data['mobile']
            )
            db.session.add(new_guest)
            db.session.commit()
            return jsonify({'message': 'guest registered successfully'}), 201
        except Exception as e:
            logging.error(f"Error registering user: {e}")
            return jsonify({"message": f"An error occurred: {e}"}), 500
    
    @app.route('/login', methods=['POST'])
    def login():
        try:
            data = request.json
            guest = Guest.query.filter_by(email=data['email']).first()
            if guest and check_password_hash(guest.password, data["password"]):
                access_token = create_access_token(
                        identity=guest.id, additional_claims={"role": guest.role})
                return jsonify({'message': 'guest logged in successfully', 'access_token': access_token}), 200
            
            return jsonify({'message': 'Invalid credentials'}), 401
        except Exception as e:
            logging.error(f"Error processing login user request: {e}")
            return jsonify({"message": f"An error occurred {e}"}), 500