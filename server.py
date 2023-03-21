from flask import Flask
from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for, jsonify)  
from model import connect_to_db, db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

cities_dict = {}
cities_list = []
place_id_list = []

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/create_user')
def create_user_form():
    return render_template('create_user.html')


@app.route('/user', methods = ['POST'])
def create_user():

    # if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password = request.form.get('password')
        user = crud.get_user_by_email(email)


        if fname=='' or lname=='' or email=='' or password=='':
            flash('Please fill out all fields')
            return redirect('create_user.html')
        elif user:
            flash('Account already exists, please log in')
            return redirect("/")
        else:
            user = crud.create_user(fname, lname, email, password)
            db.session.add(user)
            db.session.commit()
            session['fname'] = fname
            session['lname'] = lname
            session['email'] = email
            flash(f'Your account has been created successfully, {session["fname"]}!')
            return redirect ('/routes')
            


@app.route("/login", methods=["POST"])
def login():

    email = request.form.get('email')
    password = request.form.get('password')
    user = crud.get_user_by_email(email) 
        
    if user and user.password==password:
        session["user"] = user.user_id
        session['fname'] = user.fname
        session['lname'] = user.lname
        session['email'] = user.email
        
        flash(f'You are logged in! {session["fname"]}')
        return redirect('/routes')

    else:
        flash('Login unsuccessful. Please try again.')
        return redirect('/')
    

    
@app.route("/createcity", methods=['GET', 'POST'])
def create_city():
    
    if request.method=='POST': 

        cities_dict = request.json

        for key in cities_dict:
            city_name = cities_dict[key]['city']
            country = cities_dict[key]['country']
            place_id = cities_dict[key]['placeId']
            lat = cities_dict[key]['cityLat']
            long = cities_dict[key]['cityLng']
            #add them to session!!!!!
            cities_list.append(city_name)
            place_id_list.append(place_id)
            
            

            city = crud.create_city(city_name, country, place_id, lat, long)
            print('this should be object data: ', city)

        session["placeid_list"] = place_id_list

        cities = ', '.join(cities_list)
        placesid = ', '.join(place_id_list)
        
        session["cities"] =cities
        session["placesid"] =placesid
        print('this should be cities list: ', cities)
        print('this should be place list: ', placesid)
       
    
    return cities==session["cities"], placesid==session["placesid"]

@app.route("/createtrip", methods=["POST"])
def create_trip():
    email = session["email"]
    user = crud.get_user_by_email(email) 
    title = request.form.get('title')
    month = request.form.get('month')
    year = request.form.get('year')

    session["title"] = title
    trip = crud.create_trip(user, title, session["cities"], session["placesid"], month, year)

    trip= crud.get_trip_by_id(11)
    
    title1 = trip.title
    cities = trip.cities_in_order
    placeid = trip.placeid
    month1 = trip.month
    year1 = trip.year
    print('Aqui', title1, cities, placeid, month1, year1)

   
    return render_template('trip.html')

# create another route to get trip id send info to my front end, get method
@app.route('/gettrip/<trip_id>')
def get_trip():
    trip_id = request.view_args['trip_id']
    trip= crud.get_trip_by_id(trip_id)
    
    title = trip.title
    cities = trip.cities_in_order
    placeid = trip.placeid
    month = trip.month
    year = trip.year
    
    # request form from route

    return title==title, cities==cities, placeid==placeid, month==month, year==year 

    
    
    

@app.route("/routes")
def routes():
    return render_template('routes.html')

@app.route("/newtrip")
def newtrip():
    return render_template('newtrip.html')

@app.route('/trips')
def trips():
    trips = crud.return_trips()

    return render_template('all_trips.html', trips=trips)

@app.route('/trips/<trip_id>')
def trip_detail(trip_id):

    trip = crud.get_trip_by_id(trip_id)

    return render_template('trip_details.html', trip=trip)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)



