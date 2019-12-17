# CMS API



## Getting Started



### Prerequisites

What things you need to install the software and how to install them 

```
$ pip install virtualenv
(virtualenv)$ pip install -r requirements.txt
```
## Note: Is required a .env file but is added only for demo 

```
FLASK_APP=''
FLASK_ENV=''
SECRET_KEY=''
PORT=5000
HOST=''
API_KEY=''
API_URL=''
APP_NAME=''

```

### Running


``` 
$ flask run

```


## Running the tests

how to run the automated tests for this system


```
$ pytest -r cms_api/test

```



## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:5000/api/v1/*

Class | HTTP request | Description
------------ | ------------- | -------------
*Activities* | **POST** /activity | Add a new activity
*Activities* | **GET** /activities | Finds activity by status
*Activities* | **GET** /activities/{activity_id} | Find activity by ID
*Activities* | **PUT** /activities/{activity_id} | Uploads activity by ID
*Activities* | **DELETE** /activities/{activity_id} | Delete activity by ID
*Deals* | **POST** /deals | Add a new deals
*Deals* | **GET** /deals | Finds deals by status
*Deals* | **GET** /deals/{deals_id} | Find deals by ID
*Deals* | **PUT** /deals/{deals_id} | Uploads deals by ID
*Deals* | **DELETE** /deals/{deals_id} | Delete deals by ID
*Persons* | **POST** /persons | Add a new persons
*Persons* | **GET** /persons | Finds persons by status
*Persons* | **GET** /persons/{persons_id} | Find persons by ID
*Persons* | **PUT** /persons/{persons_id} | Uploads persons by ID
*Persons* | **DELETE** /persons/{persons_id} | Delete persons by ID






## Built With

* [FLASK](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [PYTEST](https://maven.apache.org/) - Unit test
* [SWAGGER](https://rometools.github.io/rome/) - Api design
