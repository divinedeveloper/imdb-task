# imdb-task
RESTful API for movies, something similar to IMDB

# Requirements 
Python 3.6
Django 3.0.7

# Clone the directory to desired folder
cd imdb-task

# Create virtual environment and activate it
virtualenv -p python3 env
source env/bin/activate

# Pip install requirements
pip install -r requirements.txt

cd movies/

# Run Migrations
python manage.py makemigrations
python manage.py migrate

# Populate the database by running following custom django admin command
python manage.py populate_db

# Run the server
python manage.py runserver

# Testing the api

1- Admin access is enabled by using the admin section provided by default

https://go-fynd-imdb.herokuapp.com/admin/

Login using credentials provided in the email

Now we can Create, edit and remove movies, also additionally we can search movies by names and filter using genres
we can also add, edit and remove Genres and can search them using genre name

2- Users can view movies using following set of apis

view all movies - https://go-fynd-imdb.herokuapp.com/api/movies

OR 

search movies by name - https://go-fynd-imdb.herokuapp.com/api/movies?search=titanic

OR

search movies with pagination - https://go-fynd-imdb.herokuapp.com/api/movies?search=war&limit=10&offset=0

OR

search movies by genre - https://go-fynd-imdb.herokuapp.com/api/movies?search=War

OR

# Multiple search parameters can be separated by using white space or comma

search movies by name and genre - https://go-fynd-imdb.herokuapp.com/api/movies?search=the,war

OR

search movies by name and director - https://go-fynd-imdb.herokuapp.com/api/movies?search=titanic,james

OR

search movies by name and director and popularity and imdb score - https://go-fynd-imdb.herokuapp.com/api/movies?search=the,john,70,7

OR

search movies by all parameters with pagination - https://go-fynd-imdb.herokuapp.com/api/movies?search=the,john,70,7,war&limit=10&offset=0



# Handling the Scaling Problem:-
1- Infrastructure changes :-
    a- splitting the api (app) into microservices
    b- using docker for prod deployment
    c- Kubernetes to manage containers and number of replicas
    d- In terms of maintenance without service down time we should be able to uprade and downgrade server resources independently
    e- metric collection and monitoring in terms of requests per microservice, cpu usages on each pods and kubernetes nodes, inbound, outbound traffic, database and storage cpu usage.
    f- Using Nginx asynchronous server and load balancing to handle requests 

2- Database changes:-
    a- choosing the right database and Database engine and should have track record of performance. Since this application is read heavy and doesnt need transaction we can think of using a NoSQL DB like MongoDB or a search Engine like Elastic Search
    b- we should focus on fast retrieval and CPU cores
    c- Profiling queries to ensure they run in less than 20ms
    d- Indexing for all queries and deleting unused or duplicate indexes
    e- Using persistent database connections to handle large number of requests
    f- Horizontal scaling the databases using sharding and replication

3- Ignoring unsed apps and middlewares in Django:-
    a- As we use REST API we can ignore sessions and messages in djangos installed apps and middlewares

4- Reducing the data transfer from DB to API and to clients:-
    a- Using orm queries with selecting only needed fields and ignoring the rest will reduce data traffice
    b- As we use JSON to transfer data which is not the most efficient way which should try reducing it too.

