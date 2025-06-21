# TEDx Project

A Django-based web application with user registration, login, role-based dashboards, and Google authentication.


This project is a full-stack web application built using Django, designed to manage TEDx events with secure user authentication and role-based access. It leverages Django's built-in authentication system, extends it with `django-allauth` for Google OAuth integration, and uses Django REST Framework along with JWT (`djangorestframework-simplejwt`) for API authentication. The app supports user registration with role selection (Admin/User), separate dashboards for each role, and a simple SQLite database for storage. Environment variables are managed with `python-dotenv` for security and flexibility. The project structure and templates are organized for

## Features

- User registration with role selection (Admin/User)
- Login and logout functionality
- Role-based dashboards (Admin and User)
- Google OAuth authentication via `django-allauth`
- SQLite database (default)
- Django REST Framework JWT authentication endpoints

## Requirements

Install dependencies using pip:

```sh
pip install -r requirements.txt
```

Main requirements include:
- Django
- django-allauth
- djangorestframework
- djangorestframework-simplejwt
- python-dotenv
- asgiref
- certifi

See [`requirements.txt`](requirements.txt) for the full list.

## Project Structure

```
tedxproject/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── .env
├── tedxapp/
│   └── ...
├── tedxproject/
│   └── urls.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── admin_dashboard.html
│   └── user_dashboard.html
└── ...
```

## URL Endpoints

Defined in [`tedxproject/urls.py`](tedxproject/tedxproject/urls.py):

- `/admin/` — Django admin
- `/accounts/` — Allauth authentication (Google, etc.)
- `/tedxapp/` — App-specific URLs
- `/api/auth/register/` — Register API ([`RegisterView`](tedxproject/tedxproject/urls.py))
- `/api/auth/login/` — Login API ([`LoginView`](tedxproject/tedxproject/urls.py))
- `/api/token/` — JWT obtain pair ([`TokenObtainPairView`](tedxproject/tedxproject/urls.py))
- `/api/token/refresh/` — JWT refresh ([`TokenRefreshView`](tedxproject/tedxproject/urls.py))

## Templates

- [`index.html`](tedxproject/templates/index.html): Home page with links to login and signup
- [`login.html`](tedxproject/templates/login.html): Login form
- [`register.html`](tedxproject/templates/register.html): Registration form with role selection and Google signup
- [`admin_dashboard.html`](tedxproject/templates/admin_dashboard.html): Admin dashboard
- [`user_dashboard.html`](tedxproject/templates/user_dashboard.html): User dashboard

## Running the Project

1. Activate your virtual environment:

    ```sh
    source Scripts/activate  # On Windows: Scripts\activate.bat
    ```

2. Apply migrations:

    ```sh
    python manage.py migrate
    ```

3. Run the development server:

    ```sh
    python manage.py runserver
    ```

4. Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

## Environment Variables

Create a `.env` file in the project root for sensitive settings (e.g., secret keys, database config).

---

For more details, see the code
