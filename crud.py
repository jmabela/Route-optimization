"""CRUD operations."""

from model import db, User, Trip, City, connect_to_db


def create_user(fname, lname, email, password):
    """Create and return a new user."""

    user = User(fname=fname, lname=lname, email=email, password=password)

    return user

def return_users():
    """Returns all users."""

    return User.query.all()


def get_user(user_id):
    """Get user by id."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """"Get user by email."""
    
    return User.query.filter(User.email == email).first()

def create_trip(user, title, cities_in_order, placeid, month, year):
    """Create and return a new trip."""

    trip = Trip(user=user, title=title, cities_in_order=cities_in_order, placeid=placeid, month=month, year=year)
    db.session.add(trip)
    db.session.commit()
    
    return trip

def return_trips():
    """Returns all trips."""

    return Trip.query.all()

def return_trip_by_id():

    return Trip.query.filter(Trip.trip_id==11).all()


def get_trip_by_id(trip_id):
    """Returns trip object when passed a trip id."""

    return Trip.query.get(trip_id)

def get_trips_by_user(user_id):
    """Returns all trips by User."""
    

    return Trip.query.filter_by(User.user_id==user_id).all()

def get_trips_by_year(year):
    """"Returns all trips by Year."""


    return Trip.query.filter_by(year).all()

def create_city(name, country, place_id, lat, long):
    """Create and return a new city."""

    city = City(name=name, country=country, place_id=place_id, lat=lat, long=long)
    db.session.add(city)
    db.session.commit()

    return city

def get_city_by_id(city_id):
    """"Returns city object when passed id"""

    return City.query.get(city_id)

def get_cities_by_country(country):

    return City.query.filter_by(country).all()





if __name__ == '__main__':
    from server import app
    connect_to_db(app)
