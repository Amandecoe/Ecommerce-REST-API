# 🎰 ALX Project Nexus

## A Fully Functional Ecommerce REST API Written in Django 

This project is a Capstone Final project for the ALX pro-dev backend program which equips you with different backend Programming skills. In this Project I have built an Ecommerce REST API with JWT authentication and then deployed it on a Live PostgreSQL server on Railway with Celery background task automation using RabbitMQ as a Broker. This project show you how to do the following:

* Design your Database Models Using Django
* Design Your Database ERD in Draw.io to present it visually
* Customize your Django Settings to Use JWT Authentication to Authenticate Users accessing the System.
* Create Easy and Maintainable Views and Serializers for Your app
* How to use signals on your REST API 
* Email notifications after a purchase is made
* Customize your Django Settings inorder to use SQLite3 for production and PostgreSQL for deployment in your database configuration

## 🏧 How to install this Project on Your Machine

### 1.🌀Clone the project
  ```bash
    git clone https://github.com/Amandecoe/alx-project-nexus.git
       cd your-repo
  ```
### 2.☢️Activate the Production Environment
   For Windows 
   ```bash
     - ecommerceEnv/Scripts/activate.bat
   ```  
   For Mac/Linux
   ```bash
     - source/ecommerceEnv/Scripts/activate
   ```

### 3.🔠Install these dependencies on your machine 
   ```bash
   - pip install django, djangorestframework, pillow, djangorestframework-simplejwt
   ```

### 4.🏃Run Migrations
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

### 5.🏡Create SuperUser (Admin)
 ```bash
 python manage.py createsuperuser
 ```

### 6.🧘 Run the Development Server
 ```bash
 python manage.py runserver
 ```

 * Access Django Admin : http://127.0.0.1:8000/admin

## Celery Setup

### This guide explains how to set up Celery with RabbitMQ for background tasks in the EcommerceApi Django project, including sending order confirmation emails and weekly newsletters.

### 1.🔠 Install Required Packages
  ```
 pip install celery
 pip install django-celery-beat
 pip install rabbitmq-server
```
### 2.🏌️‍♀️ Configure RabbitMQ
 #### 1. Start RabbitMQ
  ``` Linux/Mac
       sudo service rabbitmq-server start
      Windows
       Open Services, find RabbitMQ, right-click → Start
  ```
  ### 2. Verify RabbitMQ is Running
  ``` bash
   rabbitmqctl status
  ```       

