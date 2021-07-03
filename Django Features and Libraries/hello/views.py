from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def myview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4: del(request.session['num_visits'])
    resp = HttpResponse("Hello, world. You're at the new Hello page. c81515bd. view count="+str(num_visits))
    resp.set_cookie('dj4e_cookie', 'c81515bd', max_age=1000)
    return resp

