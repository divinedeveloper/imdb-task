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
