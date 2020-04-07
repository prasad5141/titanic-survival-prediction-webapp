# Titanic-survival-prediction-webapp
Django webapp integrated with machine learning model to predict the survival status of titanic passengers.

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

### Live Demo : www.titanicprediction.ml

### Tech Stack:

Technologies i used to build this project: 
* [Scikit learn](https://scikit-learn.org/stable/) - To build Machine Learning model
* [Django](https://www.djangoproject.com/) - Django Backend Framework
* [Pickle](https://pypi.org/project/pickle5/) - Pickle to save/load model to the web application environment 
* [AWS EC2]() - Django application deployed on AWS EC2
* [Free Template](https://bootstrapmade.com/demo/Maundy/) - Template startercode from Bootstrapmade.com
* Using [Nginx, Gunicorn, Supervisor]() in AWS Instance to serve the project.



### Installation

This project requires [Python 3.6](https://www.python.org/) or more.

Clone the repository than execute below commands and make sure virtualenv activated
```sh
$ cd titanic-survival-prediction-webapp 
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver 
```

Then go to http://127.0.0.1:8000.

You will see below like screen.

![alt text](https://raw.githubusercontent.com/prasad5141/titanic-survival-prediction-webapp/master/static/img/Capture.PNG)
