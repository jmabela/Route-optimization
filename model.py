"""Data model for routes."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from datetime import datetime

#---------------------------------------------------------------------#

class User(db.Model):
    """User data."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(25), nullable=True)
    lname = db.Column(db.String(25), nullable=True)
    email = db.Column(db.String(25), nullable=True, unique = True)
    password = db.Column(db.String, nullable=True)
    trip = db.relationship('Trip', back_populates='user')
    city = db.relationship('City', back_populates='user')

    def __repr__(self):
         

        return f"<User fname={self.fname} lname={self.lname} email={self.email}>"

class Trip(db.Model):
    """Trips data"""

    __tablename__ = "trips"

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    title = db.Column(db.String, nullable=True)
    cities_in_order = db.Column(db.String, nullable=True)
    placeid = db.Column(db.String, nullable=True)
    month = db.Column(db.String, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    
    

    user = db.relationship('User', back_populates='trip')
    


    def __repr__(self):

        return f"<Trip description={self.title}, cities in this trip={self.cities_in_order}, placesId={self.placeid} dates={self.month} to {self.year}>"

    
class City(db.Model):
    """Cities data"""
   

    __tablename__ = "cities"

    city_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    name = db.Column(db.String, nullable=True)
    place_id = db.Column(db.String, nullable=True)
    lat = db.Column(db.String, nullable=True)
    long = db.Column(db.String, nullable=True)
    country = db.Column(db.String, nullable=True)

    user = db.relationship('User', back_populates='city')
    
    


    def __repr__(self):

        return f"<City {self.name}, {self.country}>"




#---------------------------------------------------------------------#

def connect_to_db(flask_app, db_uri="postgresql:///routes", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)