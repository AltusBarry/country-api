# Technical assessment

Quick start
--------------
Browse to the root directory of this project, ie where this README is located.

Create a virtual environment using python 3.8.

	virtualenv ve -p python3.8

Activate the virtual environment

	source ./ve/bin/activate

Install requirements

	pip install -r requirements.txt

Create a local `db.sqlite3` database

	python manage.py migrate

Bootstrap that with some data

	python manage.py bootstrap_db

Run the web service locally

	python manage.py runserver

Django rest framework ships with an interactive web front-end by default this can be viewed here: http://localhost:8000/

The countries endpoint is: http://localhost:8000/countries/
Example filters:
http://localhost:8000/countries/?country=ARE
http://localhost:8000/countries/?currency=TRL
http://localhost:8000/countries/?currency=TRL&country=CYP

The currencies endpoint is: http://localhost:8000/currencies/

Testing
---------
Still in the activated virtual environment

	coverage run --source='countries' manage.py test countries
	coverage report -m

Instructions
--------------

	The company has a need for a standardised internal source of country
	information. Using Rails or a Python framework of your choice (Django, Flask,
	etc.), build a JSON REST API to provide country information.

	Requirements:

	List all countries providing at least country name, alpha 2 code, alpha 3 code
	and the currencies available. Please allow for the ability to filter on
	currency
	Return a single country based upon the alpha 2 or alpha 3 code
	An interface to allow "soft-deletion" of countries.

	Be sure to add unit tests. For the sake of simplicity, ignore any auth considerations at this point.
	Do not feel the need to spend more than 4 hours on this - we prefer tested
	features and incomplete over completed but buggy. Also, a basic solution is
	fine - no need to over engineer.
	For the country data, please feel free to use any small sample of 3-4 countries of your choice.
	If certain aspects of the task seem ambiguous, please interpret them in a way
	that makes sense to you - there is no right or wrong answer, as long as you can
	justify your solution.
