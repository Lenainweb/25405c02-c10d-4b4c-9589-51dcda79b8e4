
![python3.x](https://img.shields.io/badge/python-3.x-brightgreen.svg) ![django2.x](https://img.shields.io/badge/%20Django-2.0.1-green.svg)

## Dependencies
* Django

## Setting up

##### Clone the repo

```
$ git clone https://github.com/Lenainweb/25405c02-c10d-4b4c-9589-51dcda79b8e4.git
$ cd 25405c02-c10d-4b4c-9589-51dcda79b8e4/files_host
```

##### Initialize a virtualenv

```
$ python3.9 -m venv venv
$ . venv/bin/activate
```

##### Install the dependencies

```
$ pip install django 
```

##### Create the database

```
$ python manage.py migrate
```

## Running the server

```
$ python manage.py runserver
```


