# django_practice
first, need to creat virtual environment, then we need to install django in this virtual environment terminal

django-admin startproject myproject  // for creating project with project name "myproject"


to deactivate virtual environment--> deactivate
to activate virtual environment--> source venv/bin/activate

create urls.py file inside of myapp folder

for start server, run --> python manage.py runserver

#URL Routing and django apps
--> inside myapp folder create urls.py and create urlpatterns
--> inside myapp Create views here.

--> myproject/myproject/urls.py create urlpatterns and add path('',include('myapp.urls'))

