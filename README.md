# api_requests

Firstly, Add your Django Secret Key in "settings.py"

I used PostgreSQL for this Project. So, if you want to use the same then you have to download PostgreSQL and then change the credentials in the DATABASES section in "settings.py" after creating a database in PostgreSQL.

If you want to use the default "sqlite", then goto "settings.py" and comment-down the PostgeSQL section and uncomment the default one "sqlite".

Then, Run these commands

1. python manage.py makemigrations

2. python manage.py migrate

3. python manage.py createsuperuser

4. python manage.py runserver
