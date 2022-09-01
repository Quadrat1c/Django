# Mainly python Helpers might not be specific to Django

#includes for python
from cmath import log
from urllib import response
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import ObjectDoesNotExist

# views.py
def index(request):
  # check django version to find best practing on authenticating users in the views file
  if request.user.is_anonymous:
    return redirect("/login.html")
  else:
    context = {}
    # context can be a SQL Query to an object or API Results etc anything to an object
    return render(request, 'index.html', {'context':context})
  
# this belongs inside our default request
if filename == 'Products':
  context = GetAll('SELECT * FROM Products')
  contextCol = context[0][2] # Get specific row or column from context object
  return render(request, f"{filename}.html", {'context':context}) 

# Utility things

#from django.contrib.auth.hashers import make_password
make_password('myPasswordHere') # more arguments exists for make_password function like Hash or Encryption options

# get url parameters
urlParam = request.GET.get('paramName')

# SQL - be sure to add connections in settings instead of this technique in random files
import pyodbc
server = '192.168.1.2'
database = 'SequelDB'
username = 'root'
password = 'k8dD,c21@e3zs'

def GetAll(query):
  # ODBC Driver 17 is most common for SQL, check your ODBC Connection drivers you have installed
  con = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = con.cursor()
    # SQL Connection
    results = cursor.execute(query).fetchall()  #.fetchone()
    con.close()
    return results
