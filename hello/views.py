from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloview(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])

    cookie_value = '5e45ee43'
    resp = HttpResponse(f'view count={num_visits} (reset after 5); cookie_value: {cookie_value}')
    resp.set_cookie('dj4e_cookie', cookie_value, max_age=1000) # seconds until expire
    return resp
