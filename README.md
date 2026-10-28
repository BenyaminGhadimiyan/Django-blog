# Django Blog

A practice project built with Django: a blog with user accounts, comments and a contact form.

## Screenshot
(add a screenshot of the home page here)

## Features
- Blog posts with categories and images (list page and single-post page)
- Comments on posts, shown only after approval in the admin panel
- Contact form; messages are saved in the database
- User sign up, login and logout
- Django admin panel for managing posts, categories, comments and contact messages

## Tech stack
- Python, Django 6.1
- SQLite
- HTML, CSS, JavaScript (Bootstrap-based theme)

## Project structure
- `appMFT` – static pages (home, about, ...)
- `appBlog` – posts, categories, comments
- `appForm` – contact form
- `appAccounts` – login / signup / logout
- `MFT` – project settings and main URLs
- `templates` / `statics` – HTML templates and static files

## Run locally
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

Open http://127.0.0.1:8000/ (admin panel: /admin/).

## What I practiced
- Django models, views, forms, URLs and templates
- Foreign keys and many-to-many relations
- Handling forms and saving data
- Authentication with Django's built-in forms

## Notes
This is a learning project and is not configured for production (DEBUG is on).
The front-end theme comes from a ready-made template; the Django back-end is my own work.
