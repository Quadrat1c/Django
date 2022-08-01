# Django
Django - Python web framework

## Commands:
#### Info
```
python -m django --version
```
### Start Website
###### (:8000) can be set to your desired port
``` python manage.py runserver 0:8000 ```

### Shell
``` python manage.py shell ```

### Create app
###### Creates app directory inside project
###### (polls) set 'polls' to your desired app name
``` python manage.py startapp polls ```

### Create Super User
``` python manage.py createsuperuser ```

### Migrate
###### Define Models inside appName/models.py
###### looks at installed apps and creates database tables according to settings.py
``` python manage.py migrate ```

### Make Migrations
###### set 'polls' to your app name
###### By running makemigrations, you’re telling Django that you’ve made some changes to your models (in this case, you’ve made new ones) and that you’d like the changes to be stored as a migration.
``` python manage.py makemigrations polls```

### Sql Migrate
###### set 'polls' to your app name
``` python manage.py sqlmigrate polls 0001 ```
