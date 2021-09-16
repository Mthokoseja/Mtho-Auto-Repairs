from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<p>home view </p>')

def car_detail(request,id):
    return HttpResponse('<p>car detail view  with id {} </p>'.format(id))

