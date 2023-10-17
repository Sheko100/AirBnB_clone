# AirBnB clone - The console

A project during ALX program to make a command line interface program to manage the AirBnB clone components

## Directory Tree Structure

```
├── AUTHORS
├── console.py
├── __init__.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    ├── __init__.py
    └── test_models
        ├── __init__.py
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   └── test_file_storage.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```

## How to start the console
Just run ```./console.py``` on your command line, then you will enter the interactive mode

## How to use it
These are the command you can use:

 - create: creates a new instance
 E.G: ```Create User```
 
 - all: prints all the objects created
 - show: prints a particular object
 E.G: ```show User 66aaf9b8-6e63-4acd-96d2-389559d91dc7```
 - destroy: delets an object
  E.G: ```destroy User 66aaf9b8-6e63-4acd-96d2-389559d91dc7```
 - update: updates the attributes of the instance
 E.G: ```update User 66aaf9b8-6e63-4acd-96d2-389559d91dc7 First_name "Ali"```
