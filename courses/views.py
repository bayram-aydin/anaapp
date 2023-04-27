from django.shortcuts import render
from django.http import HttpResponse


def kurslar (request):
    return HttpResponse("Kurslar Sayfa") 
def details (request):
    return HttpResponse("Detay Sayfa") 
def programlama (request):
    return HttpResponse("Programlama Sayfa") 
def mobiluygulamalar (request):
    return HttpResponse("Mobil uygulamalar Sayfa") 
