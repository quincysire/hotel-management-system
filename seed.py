# seed.py
from app import app, db  # Import app and db from app
from models.guest import Guest
from models.hotel import Hotel


def seed_users():
    with app.app_context():  
        db.create_all()

        # # Delete existing guests (if any)
        # Guest.query.delete()
        Hotel.query.delete()

        # # Create new guests
        # user1 = Guest(
        #     firstName='John',
        #     secondName='Doe',
        #     email='john@example.com',
        #     password='password123',
        #     mobile='1234567890'
        # )
        # user2 = Guest(
        #     firstName='Jane',
        #     secondName='Smith',
        #     email='jane@example.com',
        #     password='password456',
        #     mobile='0987654321'
        # )

        hotels_data = [
            {"hotelName": "Savannah", "price": 1000, "img": "https://plus.unsplash.com/premium_photo-1661676056771-f6c2711249e0?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Paradise", "price": 15000, "img": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Baobab", "price": 20000, "img": "https://plus.unsplash.com/premium_photo-1678297269980-16f4be3a15a6?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Swahili", "price": 25000, "img": "https://images.unsplash.com/photo-1566073771259-6a8506099945?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Diani", "price": 30000, "img": "https://images.unsplash.com/photo-1618773928121-c32242e63f39?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Travellers", "price": 35000, "img": "https://images.unsplash.com/photo-1445019980597-93fa8acb246c?q=80&w=2074&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Riverside Suites", "price": 5000, "img": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Serenity Spa Resort", "price": 4000, "img": "https://images.unsplash.com/photo-1445991842772-097fea258e7b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Mountain Retreat Lodge", "price": 3500, "img": "https://images.unsplash.com/photo-1444201983204-c43cbd584d93?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Grand Palace Hotel", "price": 5500, "img": "https://plus.unsplash.com/premium_photo-1678286770016-6306ad61df9b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Ocean View Inn", "price": 40000, "img": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "City Lights Hotel", "price": 35000, "img": "https://plus.unsplash.com/premium_photo-1678286769888-ef3698e72a6c?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Sunset Boulevard Hotel", "price": 10000, "img": "https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "The Urban Oasis", "price": 5000, "img": "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Kempinski", "price": 35000, "img": "https://images.unsplash.com/photo-1498503182468-3b51cbb6cb24?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Maasai Mara Safari Camp", "price": 3000, "img": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Safari Lodge", "price": 9000, "img": "https://images.unsplash.com/photo-1600011689032-8b628b8a8747?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Serengeti Retreat", "price": 75000, "img": "https://images.unsplash.com/photo-1615460549969-36fa19521a4f?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Sahara Desert Oasis", "price": 3500, "img": "https://images.unsplash.com/photo-1519690889869-e705e59f72e1?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Okavango Delta Resort", "price": 10000, "img": "https://images.unsplash.com/photo-1596394516093-501ba68a0ba6?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Mombasa Seaside Inn", "price": 4500, "img": "https://images.unsplash.com/photo-1596436889106-be35e843f974?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Timbuktu Heritage Hotel", "price": 8000, "img": "https://images.unsplash.com/photo-1584132967334-10e028bd69f7?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Casablanca Royal", "price": 95000, "img": "https://images.unsplash.com/photo-1584132915807-fd1f5fbc078f?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "L.Baringo Spa", "price": 8500, "img": "https://images.unsplash.com/photo-1606402179428-a57976d71fa4?q=80&w=1074&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Safari Park", "price": 65000, "img": "https://images.unsplash.com/photo-1598605272254-16f0c0ecdfa5?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "BluePost Hotel", "price": 55000, "img": "https://images.unsplash.com/photo-1590381105924-c72589b9ef3f?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"},
            {"hotelName": "Lagoon Hotel", "price": 90000, "img": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"}
        ]

        # # Add and commit changes to database
        # db.session.add(user1)
        # db.session.add(user2)

        # Create hotel instances using the hotel data
        hotels = [Hotel(**data) for data in hotels_data]

        db.session.add_all(hotels)
        db.session.commit()

        print('Database seeded with initial users.')

if __name__ == '__main__':
    seed_users()