# Route-optimization

Full stack platform to help users to organize their trip. Users can create their own accounts or log in. It comes with an autocomplete search box to assist users when entering foreign locations. It uses directions services, library places from Google Maps API. The platform makes API calls with Place Id and Lat/Long depending on what the user is requesting. Users need to add their destinations without specific order -- first destination will be start and end point. The app will optimize route and give back the fastest route available for the trip. App renders a map with the optimized route and gives step by step directions of the route. User can save and come back to their previous trips



## Demo
![2023-09-25 10 39 45](https://github.com/jmabela/Route-optimization/assets/114891957/44b28b8d-4404-4048-9d62-f2f37f786c07)


https://youtu.be/RHj5W62FzbY



## Installation

Installation
Requirements:

    PostgreSQL
    Python 3.7.3

To have this app running on your local computer, please follow the below steps:

Clone repository:

    $ git clone https://github.com/jmabela/Route-optimization.git

Create and activate a virtual environment:

    $ pip3 install virtualenv
    $ virtualenv env
    $ source env/bin/activate

Install dependencies:

    (env) $ pip3 install -r requirements.txt

Create database routes:

    (env) $ createdb routes

Create database tables:

    (env) $ python3 -i model.py
    >>> db.create_all()

Start backend server:

    (env) $ python3 server.py
    
 Create a Google Maps Api key.



## Authors

- [@jmabela](https://www.github.com/jmabela)

