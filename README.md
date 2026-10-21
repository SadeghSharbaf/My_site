# My Site

A Django web application with blog-related functionality, templates, static assets, and uploaded media.

## Tech Stack
- Python
- Django

## Local Setup
1. Create and activate a virtual environment.
2. Install dependencies from the project's dependency file, if present.
3. Set required environment variables and review Django settings.
4. Run:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Media and Database
The local SQLite database is not included. User-uploaded media should be handled according to the deployment/storage configuration and should not be committed as runtime data.

## Security
Set a strong, private Django secret key and disable debug mode in production.
