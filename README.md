# Route-optimization

Introducing a sophisticated full-stack platform meticulously crafted to enhance users' trip organization capabilities. This all-encompassing system empowers users with the ability to effortlessly create accounts or log in, while featuring a cutting-edge autocomplete search box to streamline the input of foreign locations. The platform harnesses the prowess of Google Maps API, leveraging its directions services and library places, to facilitate a seamless user experience.

Through strategic API calls utilizing Place Id and Lat/Long data, the platform caters to individual user preferences. Of particular note, users can add destinations in a flexible, non-prescriptive order, with the initial destination serving as both the starting and ending point. The application then employs advanced algorithms to intelligently optimize the route, offering the swiftest itinerary available for the trip. A dynamic map interface not only displays the optimized route but also provides users with comprehensive, step-by-step directions for a hassle-free journey.

Additionally, the system offers a robust trip saving feature, allowing users to store and revisit their previous trips at their convenience. This ensures a highly personalized and efficient travel planning experience.



## Demo

Watch this video for a better understanding of the App: 

https://youtu.be/RHj5W62FzbY

Create your account:

![2023-09-25 10 39 45](https://github.com/jmabela/Route-optimization/assets/114891957/44b28b8d-4404-4048-9d62-f2f37f786c07)

Or log into your account:

![](https://github.com/jmabela/jmabela_public/blob/9d0a54877c5735d0e43ad305b0757f70416d78cd/2023-09-25%2014.03.59.gif)

Plan your route, see previous routes and find out how many cities you've been to:

![https://github.com/jmabela/jmabela_public.git/main/2023-09-26 10.37.07 2.gif](https://github.com/jmabela/jmabela_public/blob/f5743b58d475dbea7316cb8048d5512ef25028ba/2023-09-26%2010.37.07%202.gif)



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

