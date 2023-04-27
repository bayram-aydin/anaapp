from django.shortcuts import render
from django.http import HttpResponse


def kurslar (request):
    return HttpResponse("Kurslar Sayfa") 
def details (request, kurs_adi):
    return HttpResponse(f"{kurs_adi} Detay Sayfası") 

def getCoursesByCategory (request, category_name):
    text=""
    if(category_name=="programlama"):
        text="programlaam işine ait kurlar"
    elif(category_name=="web"):
        text="web işine ait kurlar"
    else:
        text= "yanlış sayfaya gidiyon canım benim"
    return HttpResponse(text) 

def getCoursesByCategoryId(request, category_id):
    return HttpResponse(category_id)
