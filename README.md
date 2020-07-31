# imdb-task
RESTful API for movies, something similar to IMDB

#Requirements 
Python 3.6
Django 3.0.7

#CLone the directory to desired folder
cd imdb-task

#Create virtual environment and activate it
virtualenv -p python3 env
source env/bin/activate

#Pip install requirements
pip install -r requirements.txt

cd movies/

#Run Migrations
python manage.py makemigrations
python manage.py migrate

#Populate the database by running following custom django admin command
python manage.py populate_db

#Run the server
python manage.py runserver

#Testing the api

1- Admin access is enabled by using the admin section provided by default
http://127.0.0.1:8000/admin
Login using credentials
swapnil
Password@123

Now we can Create, edit and remove movies, also additionally we can search movies by names and filter using genres
we can also add, edit and remove Genres and can search them using genre name

2- Users can view movies using following set of apis

view all movies - http://127.0.0.1:8000/api/movies

search movies by name - http://127.0.0.1:8000/api/movies?search=titanic

OR

search movies with pagination - http://127.0.0.1:8000/api/movies?search=war&limit=10&offset=0

OR

search movies by genre - http://127.0.0.1:8000/api/movies?search=War

OR

#Multiple search parameters can be separated by using white space or comma

search movies by name and genre - http://127.0.0.1:8000/api/movies?search=the,war

OR

search movies by name and director - http://127.0.0.1:8000/api/movies?search=titanic,james

OR

search movies by name and director and popularity and imdb score - http://127.0.0.1:8000/api/movies?search=the,john,70,7

OR

search movies by all parameters with pagination - http://127.0.0.1:8000/api/movies?search=the,john,70,7,war&limit=10&offset=0

