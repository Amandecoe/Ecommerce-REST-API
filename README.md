ALX Project Nexus

Description:
ALX Project Nexus is a robust backend API for an e-commerce platform, developed as part of the ALX ProDev Backend Engineering program. It handles product management, user authentication, cart and order processing, and reviews.

Technologies Used:

Backend: Django REST Framework

Database: PostgreSQL

Language: Python 3.13

Features:

Product catalog and category management

Shopping cart management

Order processing

Review and rating system

Admin dashboard for managing products, orders, and users

Installation
1. Clone the repository
git clone https://github.com/Amandecoe/alx-project-nexus.git
cd alx-project-nexus

2. Set up a virtual environment
python -m venv ecommerceEnv
# On Windows:
ecommerceEnv\Scripts\activate
# On macOS/Linux:
source ecommerceEnv/bin/activate

3. Install dependencies

Since there’s no requirements.txt, install manually:

pip install django djangorestframework psycopg2-binary


You may also need other packages used in the project; check import statements in the code to install missing ones.

4. Configure PostgreSQL

Install PostgreSQL on your machine.

Create a database, e.g., nexus_db.

Update settings.py in your Django project:

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

5. Apply migrations
python manage.py makemigrations
python manage.py migrate

6. Create a superuser
python manage.py createsuperuser

7. Run the server
python manage.py runserver


Access API: http://127.0.0.1:8000/
Access admin dashboard: http://127.0.0.1:8000/admin/

Contributing

Feel free to fork the repository, submit issues, and send pull requests. Contributions are welcome!