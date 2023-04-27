from django.http import HttpResponse
from django.shortcuts import render


def home (request):
    return HttpResponse("Ana Sayfa")
def hakkimizda (request):
    return HttpResponse("Hakkımızda Sayfası") 
def iletisim (request):
    return HttpResponse("İletişim Sayfası") 