"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb routes")
os.system('createdb routes')

model.connect_to_db(server.app)
model.db.create_all()



months = ['jan', 'feb', 'march', 'apr', 'may', 'jun',  'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
years = [2023, 2024, 2025]


for n in range(5):
    fname = f'User{n}'
    lname = f'Test{n}'
    email = f'user{n}@test.com'  
    password = 'test'

    user = crud.create_user(fname, lname, email, password)
    model.db.session.add(user)

    for i in range(2):
        title = choice(['summer', 'fall', 'winter', 'spring'])
        title = f'{title} {i}'
        cities_in_order = f'Lalalan {i}'
        month = choice(months)
        year=choice(years)
        placeid = 'ChIJgTwKgJcpQg0RaSKMYcHeNsQ, ChIJAVkDPzdOqEcRcDteW0YgIQQ, ChIJD7fiBh9u5kcRYJSMaMOCCwQ'
        trip = crud.create_trip(user, title, cities_in_order, placeid, month, year)
        model.db.session.add(trip)

for j in range(4):
    name= f'Lalala{j}'
    placeid= f'geolocation {j}'
    lat= i+5
    long= i+100
    country =f'Country{j}'
    city= crud.create_city(name, country, placeid, lat, long)
    model.db.session.add(city)
        
model.db.session.commit()   