# Route-optimization

Full stack platform to help users to organize their trip. Users can create their own accounts or log in. It comes with an autocomplete search box to assist users when entering foreign locations. It uses directions services, library places from Google Maps API. The platform makes API calls with Place Id and Lat/Long depending on what the user is requesting.  



## Demo

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

