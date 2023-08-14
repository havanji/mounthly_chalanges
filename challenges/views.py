from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

def january(request):
    return HttpResponseBadRequest("Eat no meat for the entire month!")

def february(request):
    return HttpResponseBadRequest("Walk for at least 20 min every day")
