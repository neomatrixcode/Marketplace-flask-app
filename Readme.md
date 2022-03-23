# Marketplace-flask-app

This project is a basic catalog system for managing products.

There are two types of users:
* admins: create/update/delete products and create/update/delete other admins

* users anonymous: users who can only retrieve product information but cannot make changes.

Whenever an admin user makes a change to a product (for example, adjusting the price), all admins are notified of the change by email.

The times that a user consults a specific product are also recorded, this with the purpose of obtaining later statistics.

## Run for the first time

The project has a docker container, to which you have to specify the location of the database, and the AWS credentials since it uses the Amazon SES service to send emails.

The project has migration commands to create the tables if needed.

```bash
docker build -t marketplace .

docker run -it --rm -p 80:80
-e REGION_NAME=us-east-1
-e AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXX
-e EMAIL_SOURCE=josuecevedo@gmail.com
-e AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXX
-e DATABASE_URL=mysql://root:root@192.168.1.67:3306/db
-v "C:\Users\josue\Desktop\Marketplace-flask-app\backend":/app marketplace bash

bash-5.1# # Run migrations
bash-5.1# flask db init
bash-5.1# flask db migrate
bash-5.1# flask db upgrade
bash-5.1# # Run nginx
bash-5.1# nginx && uwsgi --ini /app.ini
```

# Routes

## End-point: http://127.0.0.1/users/login
### Method: POST
>```
>http://127.0.0.1/users/login
>```
### Body (**raw**)

```json
{
    "email":"josuecevedo@gmail.com",
    "password": "rgu7ue56ie"
}
```
## Return

```json
{
    "Token": "rccdcdegdue7f347ugudpwc7eoiw"
}
```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/products
### Method: GET
>```
>http://127.0.0.1/api/products
>Header: Autorization: Bearer Token
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/products/crgf6p7id
### Method: GET
>```
>http://127.0.0.1/api/products/crgf6p7id
>Header: Autorization: Bearer Token
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/products
### Method: POST
>```
>http://127.0.0.1/api/products
>Header: Autorization: Bearer Token
>```
### Body (**raw**)

```json
{
"sku" : "d7iy6euiue",
"name" : "zapatos",
"price" : 300,
"mark" : "chabelo",
"quantity" : 5
 }
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/products/crgf6p7id/
### Method: PUT
>```
>http://127.0.0.1/api/products/crgf6p7id/
>Header: Autorization: Bearer Token
>```
### Body (**raw**)

```json
{
    "price": 500
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/products/crgf6p7id/
### Method: DELETE
>```
>http://127.0.0.1/api/products/crgf6p7id/
>Header: Autorization: Bearer Token
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/users
### Method: GET
>```
>http://127.0.0.1/api/users
>Header: Autorization: Bearer Token
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/users/1
### Method: GET
>```
>http://127.0.0.1/api/users/1
>Header: Autorization: Bearer Token
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/users
### Method: POST
>```
>http://127.0.0.1/api/users
>Header: Autorization: Bearer Token
>```
### Body (**raw**)

```json
{
 "fullname": "arnoldo",
 "password": "cheutere",
 "username": "marado",
 "email": "josuecevedo@xd.com",
 "rol": 2
 }
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/users/6/
### Method: PUT
>```
>http://127.0.0.1/api/users/6/
>Header: Autorization: Bearer Token
>```
### Body (**raw**)

```json
{
    "rol": 1
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: http://127.0.0.1/api/users/6
### Method: DELETE
>```
>http://127.0.0.1/api/users/6/
>Header: Autorization: Bearer Token
>```

⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

# Deploy

if you want to deploy your project on AWS, you can use terraform to create an EC2 cluster from a docker image stored on Amazon ECR.
Create and set a bucket name in the terraform.tf file.


# Comments

The project assumes that it is a buying and selling site, similar to Amazon or Mercado Libre, so the analysis of the products bought and viewed is important to determine product recommendation strategies as well as their demand and supply.

The time logs of users viewing the products could be analyzed by data-flow systems so that their analysis does not overload system demand. Being able to count on an analysis dashboard with tools such as grafana and elasticSearch

The same with the mail notification service, which would be processed asynchronously in a message queue.

You could have replicas of the databases, to improve reliability by increasing the number of application users.

Through automatic scaling services, the number of containers would be increased with respect to demand.
