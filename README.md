# ALX Project Nexus

A Scalable E-Commerce Backend API built with Django REST Framework

## Table of Contents

Project Overview

Technologies

Features

Installation

Usage

Contributing

License

### Project Overview

ALX Project Nexus is a production-ready backend API for an e-commerce platform.
It provides all the core functionalities needed for online shopping applications, including:

User registration and authentication

Product and category management

Shopping cart and order processing

Review and rating system

Admin dashboard for managing products, orders, and users

This project was developed as part of the ALX ProDev Backend Engineering program.

### Technologies

Backend: Django REST Framework

Database: PostgreSQL

Authentication: JWT (JSON Web Tokens)

Programming Language: Python 3.13

### Features

User Authentication & Authorization: Secure user signup/login with JWT

Product Management: CRUD operations for products and categories

Shopping Cart: Add, update, and remove products in cart

Orders: Create and manage orders

Reviews & Ratings: Users can review products once and update them

Admin Dashboard: Full control of products, orders, and users

### Installation
1. Clone the Repository
git clone https://github.com/Amandecoe/alx-project-nexus.git
cd alx-project-nexus

2. Create a Virtual Environment
python -m venv ecommerceEnv

# Windows
ecommerceEnv\Scripts\activate

# macOS/Linux
source ecommerceEnv/bin/activate

3. Install Dependencies

Since there’s no requirements.txt, install manually:

pip install django djangorestframework psycopg2-binary


You may need to install additional packages depending on your project setup.

### 4. Configure PostgreSQL

Install PostgreSQL.

Create a database, e.g., nexus_db.

Update settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nexus_db',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

6. Create a Superuser
python manage.py createsuperuser

7. Run the Server
python manage.py runserver


API Root: http://127.0.0.1:8000/

Admin Dashboard: http://127.0.0.1:8000/admin/

### Usage

Use Postman or any API client to test endpoints.

Authenticate users via JWT to access protected routes.

Add products to cart, place orders, and leave reviews.

### Contributing

Contributions are welcome!

Fork the repository

Create a new branch (git checkout -b feature/YourFeature)

Commit your changes (git commit -m 'Add new feature')

Push to the branch (git push origin feature/YourFeature)

Open a Pull Request