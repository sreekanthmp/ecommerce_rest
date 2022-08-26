# ecommerce-backend

Django backend for eCommerce project. This project is built using Django REST Framework 
to provide the backend API for eCommerce project.

## Main requirements

1)python 

2)Django

3)PostgreSQL 

##  API Endpoints

### Register

Method: POST

Endpoint: /registration

Payload:
{"username": "USERNAME", "password1": "PASSWORD", "password2": "PASSWORD",
"email": "EMAIL", 'first_name':"FIRST_NAME", 'last_name':"LAST_NAME" }

### Login

Method: POST

Endpoint: /login

Payload:
{ "username": "USERNAME", "password": "PASSWORD" }

### Product

Method: POST

Endpoint: /product

Payload:
{"product_name":"PRODUCT","price":"PRICE"}

### Order

Method: POST

Endpoint: /myorder

Payload:
{"product":"PRODUCT","address":"ADDRESS"}

### Cart

Method: POST

Endpoint: /mycart

Payload:
{"product":"PRODUCT","count":"Count"}


### Cartorder

Method: POST

Endpoint: /cartorder

Payload:
{"address":"ADDRESS"}







