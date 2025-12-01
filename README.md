
# A Fully Functional Ecommerce REST API Written in Django 

This project is a Capstone Final project for the ALX pro-dev backend Program. In this Project I have built an Ecommerce REST API with JWT authentication and then deployed it on a Live PostgreSQL server on Docker with Celery background task automation using RabbitMQ as a Broker. Some of the tasks done in this Project:

* Design your Database Models Using Django
* Design Your Database ERD in Draw.io to present it visually
* Customize your Django Settings to Use JWT Authentication to Authenticate Users accessing the System.
* Create Easy and Maintainable Views and Serializers for Your app
* How to use signals on your REST API 
* Email notifications after a purchase is made
* Weekly newsletters implementation using Celery beat and RabbitMQ
* Customize your Django Settings inorder to use PostgreSQL for deployment in your database configuration

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

### This guide explains how to set up Celery with RabbitMQ for background tasks in the EcommerceApi Django project, including sending order confirmation emails and weekly newsletters through email.

### 1.🔠 Install Required Packages
  ```
 pip install celery
 pip install django-celery-beat
 pip install rabbitmq-server
```
### 2.🏌️‍♀️ Configure RabbitMQ
 #### 1. Start RabbitMQ
  ``` 
  Linux/Mac
       sudo service rabbitmq-server start
  Windows
       Open Services, find RabbitMQ, right-click → Start
  ```
  #### 2. Verify RabbitMQ is Running
  ``` bash
   rabbitmqctl status
  ```       
### 3.📧 Configure Django Email Settings

Add in settings.py (example using Gmail SMTP):
```
 EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
 EMAIL_HOST = "smtp.gmail.com"
 EMAIL_PORT = 587
 EMAIL_USE_TLS = True
 EMAIL_HOST_USER = "your_email@gmail.com"
 EMAIL_HOST_PASSWORD = "your_16_char_app_password"  # App Password, no spaces
 DEFAULT_FROM_EMAIL = "your_email@gmail.com"
```
### 4. Run Celery Worker and Beat
Open two terminals:
 ```
  celery -A EcommerceApi worker -l info --pool=solo
  ```
 ```
 celery -A EcommerceApi beat -l info
 ```

## Tips
   * Use environment variables for sensitive info (EMAIL_HOST_PASSWORD).
   * Always run RabbitMQ, Celery worker, and Celery Beat before triggering tasks.
   * Celery Beat handles scheduled tasks (like weekly newsletters).
