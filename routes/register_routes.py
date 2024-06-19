from routes.auth import auth
from routes.hotel_routes import hotel_routes

def register_routes(app, db):

    @app.route("/", methods=["GET"])
    def welcome():
        return "Welcome to Hotel Bookings APIs."
    
    auth(app, db)

    hotel_routes(app, db)