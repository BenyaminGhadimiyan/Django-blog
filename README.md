# Django Blog

A practice project built with Django: a simple blog with user accounts and a contact form.

## Features
- Blog: posts with categories and an image, list page and single-post page
- Comments on posts (shown only after approval in the admin panel)
- Contact form (messages are saved in the database)
- User sign up, login and logout
- Django admin panel for managing posts, categories, comments and contact messages

## Project structure
- `appMFT` – static pages (home, about, ...)
- `appBlog` – posts, categories, comments
- `appForm` – contact form
- `appAccounts` – login / signup / logout
- `MFT` – project settings and main URLs
- `templates` / `statics` – HTML templates and static files

## Run locally
```
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Then open http://127.0.0.1:8000/ (admin panel: /admin/).

## Notes
This is a learning project and is not configured for production (DEBUG is on, SQLite database).
The front-end template (HTML/CSS/JS, fonts, Bootstrap) comes from a ready-made theme; the Django back-end is my own work.
