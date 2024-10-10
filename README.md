# Django Ninja Starter Project - Django 4.2

This project is a starter template for building CRUD applications using Django and Django Ninja. It provides a basic setup with Django for the backend and Django Ninja for creating APIs. This project does not include any frontend templates, focusing solely on the backend.

## Demo Project

A live demo of the project is available at <a href="https://startproject-django-ninja-demo.onrender.com/api/docs" target="_blank">https://startproject-django-ninja-demo.onrender.com/api/docs</a>.

### Demo Credentials
- **Username:** testuser
- **Password:** demo1234

## Testing API Routes with Postman
Here’s how you can test the provided API routes using Postman:

### 1. User Login

- **URL**: `https://startproject-django-ninja-demo.onrender.com/api/users/login`
- **Method**: POST
- **Body** (JSON):
  ```json
  {
    "username": "testuser",
    "password": "demo1234"
  }
  ```

- **Response**:
  - `200 OK`: The response will include an access token. Copy this token for use in subsequent requests.

### 2. User Logout

- **URL**: `https://startproject-django-ninja-demo.onrender.com/api/users/logout`
- **Method**: `POST`
- **Headers**:
  - `Authorization`: `Bearer <your_access_token>`


### 3. Get Clients

- **URL**: `https://startproject-django-ninja-demo.onrender.com/api/clients/`
- **Method**: `GET`
- **Headers**:
  - `Authorization`: `Bearer <your_access_token>`

### 4. Add Client

- **URL**: `https://startproject-django-ninja-demo.onrender.com/api/clients/add`
- **Method**: `POST`
- **Headers**:
  - `Authorization`: `Bearer <your_access_token>`
- **Body** (JSON):
  ```json
  {
    "company_name": "Vertex Solutions",
    "first_name": "Mia",
    "last_name": "Taylor",
    "position": "UX Designer",
    "phone": "+1-555-876-5432",
    "email": "mia.t@vertex.com",
    "website": "https://vertex.com",
    "address": "321 Cedar St",
    "city": "Denver",
    "state": "CO",
    "zipcode": "80202"
  }
  ```

### 5. View Client

- **URL**: `https://startproject-django-ninja-demo.onrender.com/api/clients/{pk}`
- **Method**: `GET`
- **Headers**:
  - `Authorization`: `Bearer <your_access_token>`

### 6. Update Client

- **URL**: `https://startproject-django-ninja-demo.onrender.com/api/clients/edit/{pk}`
- **Method**: `PUT`
- **Headers**:
  - `Authorization`: `Bearer <your_access_token>`
- **Body** (JSON):
  ```json
  {
    "company_name": "Vertex Solutions",
    "first_name": "Mia",
    "last_name": "Taylor",
    "position": "UX Designer",
    "phone": "+1-555-876-5432",
    "email": "mia.t@vertex.com",
    "website": "https://vertex.com",
    "address": "321 Cedar St",
    "city": "Denver",
    "state": "CO",
    "zipcode": "80202"
  }
  ```

### 7. Delete Client

- **URL**: `https://startproject-django-ninja-demo.onrender.com/api/clients/delete/{pk}`
- **Method**: `DELETE`
- **Headers**:
  - `Authorization`: `Bearer <your_access_token>`

### Summary

- **Login**: Obtain the JWT token by making a POST request to `/api/users/login/`.
- **Authorization**: Add the `Authorization` header with the Bearer token in Postman for all subsequent requests.
- **Test Routes**: Use the provided URLs and methods to test the GET, POST, PUT, and DELETE operations on the clients endpoint.

By following these steps, you can test the API routes of your Django Ninja Starter Project on Render using Postman.


### Note
The project is hosted on a free instance web service on Render. As a result, it may be idle sometimes, causing the initial load to be slow. However, once the application is loaded, it should work normally.

### Features

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **Django Ninja**: A web framework for building APIs with Django and Python 3.6+ type hints.
- **CRUD Operations**: Basic Create, Read, Update, and Delete operations using Django models and Django Ninja APIs.


### Example Model in Client App

The `client` app includes a simple model to demonstrate how to define and use models in Django. Here's an example of the `Client` model:

```python
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name
```


## Prerequisites

Ensure you have the following installed on your machine:
- Python (3.x recommended)
- Node.js and npm
- pyenv (optional but recommended for managing Python versions)

## Setup Instructions

Follow these steps to set up the project locally:

### 1. Clone the Repository

```bash
git clone git@github.com:igortosic-easymind/startproject-django-ninja.git
cd startproject-django-ninja
```

### 2. Set Up Python Virtual Environment
Using pyenv to set up a virtual environment ensures that the project dependencies are isolated from your global Python environment.

```bash
pyenv exec python3 -m venv .venv
```

### 3. Activate the Virtual Environment
Activate the virtual environment to start using it. This step is crucial before installing dependencies and running the project.

For macOS and Linux:
```bash
source .venv/bin/activate
```
For Windows:
```bash
.venv\Scripts\activate
```

### 4. Install Python Dependencies
Install all required Python packages listed in requirements.txt.

```bash
pip3 install -r requirements.txt
```

### 5. Create a Superuser
After cloning the repository, you need to create a superuser for your database. This is necessary to access the Django admin interface and manage your application.

To create a superuser, run the following command:

```bash
python3 manage.py createsuperuser
```

### 6. Run Migrations
Apply the database migrations to set up your database schema.

```bash
python3 manage.py migrate
```

### 7. Run the Development Server
Start the Django development server to begin working on your project.

```bash
python3 manage.py runserver
```

Additional Commands
Deactivate the Virtual Environment: When you are done working on the project, you can deactivate the virtual environment by simply running:

```bash
deactivate
```

## Database Configuration

In the `settings.py` file, the default database settings for SQLite3 are commented out. There are settings for PostgreSQL which also require a `.env` file for local development. You can choose which one you want to use based on your preference.

### Using SQLite3
To use SQLite3, uncomment the relevant lines in the `settings.py` file.

### Using PostgreSQL
To use PostgreSQL, ensure you have a `.env` file with the necessary database configuration. The `DATABASE_URL_EXT` variable should be set in the `.env` file to configure the PostgreSQL connection.


## Contributing

If you wish to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-branch
    ```
3. Make your changes.
4. Commit your changes:
    ```bash
    git commit -am 'Add new feature'
    ```
5. Push to the branch:
    ```bash
    git push origin feature-branch
    ```
6. Create a new Pull Request.

License
This project is licensed under the free License. See the LICENSE file for more details.
