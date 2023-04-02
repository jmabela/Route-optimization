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
            return redirect('/create_user')
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
            # flash(f'Your account has been created successfully, {session["fname"]}!')
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
        
        # flash(f'You are logged in! {session["fname"]}')
        return redirect('/routes')

    else:
        flash('Login unsuccessful. Please try again.')
        return redirect('/')
    

    
@app.route("/createcity", methods=['GET', 'POST'])
def create_city():
    
    # if request.method=='POST': 

        email = session["email"]
        user = crud.get_user_by_email(email) 

        cities_dict = request.json
        title = cities_dict["title"]
        month= cities_dict['month']
        year= cities_dict['year']
        
        del cities_dict["title"], cities_dict["month"], cities_dict["year"]
        

        for key in cities_dict:
            city_name = cities_dict[key]['city']
            country = cities_dict[key]['country']
            place_id = cities_dict[key]['placeId']
            lat = cities_dict[key]['cityLat']
            long = cities_dict[key]['cityLng']
            #add them to session!!!!!
            cities_list.append(city_name)
            place_id_list.append(place_id)
            city = crud.create_city(user, city_name, country, place_id, lat, long)
            print('this should be object data: ', city)

        session["placeid_list"] = place_id_list

        cities = ', '.join(cities_list)
        placesid = ', '.join(place_id_list)
        
        session["cities"] =cities
        session["placesid"] =placesid

        trip = crud.create_trip(user, title, cities, placesid, month, year)
       
    
        return render_template('trip.html')

@app.route("/createtrip", methods=["POST"])
def create_trip():
   
    return render_template('trip.html')


@app.route("/routes")
def routes():
    return render_template('routes.html')

@app.route("/newtrip")
def newtrip():
    return render_template('newtrip.html')

@app.route('/trips')
def trips():
    email = session["email"]
    user = crud.get_user_by_email(email) 
    trips = crud.get_trips_by_user(user.user_id)

    return render_template('all_trips.html', trips=trips)

@app.route('/trips/<trip_id>')
def trip_detail(trip_id):

    trip = crud.get_trip_by_id(trip_id)

    
    if trip  == None:
        

        return redirect('/routes')
    
    else:

        return render_template('trip_details.html', trip=trip)
    
@app.route('/cities-visited')
def cities_visited():
    email = session["email"]
    user = crud.get_user_by_email(email)
    cities = crud.get_cities_by_user(user.user_id)
    places_id = []
    for i in range(len(cities)):
        place_id = cities[i].place_id
        places_id.append(place_id)

    places_id_set = set(places_id)
    places_id = list(places_id_set)

    session["places_id"]=places_id
   
    

    return render_template('citiesvisited.html', cities=cities)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)



