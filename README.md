# Django

## The "Nuclear" Option (Development only):

If you don't care about the data currently in your database:

- Delete the db.sqlite3 file (or drop your local database).
- Delete all files in your app_name/migrations/ folder except **init**.py.
- Run python manage.py makemigrations and `python manage.py migrate`
- Recreate your superuser: `python manage.py createsuperuser`
