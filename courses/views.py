from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    return HttpResponse("Ana Sayfa")
def kurslar (request):
    return HttpResponse("Kurslar Sayfa") 