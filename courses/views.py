from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse

data = {
    "programlama":"programlaam işine ait kurlar",
    "web":"web işine ait kurlar",
    "mobil":"mobil işine ait kurlar işine ait kurlar",
}

def index (request):
    return render(request, "courses/index.html")
def kurslar (request):
    return HttpResponse("Kurslar Sayfa") 
def details (request, kurs_adi):
    return HttpResponse(f"{kurs_adi} Detay Sayfası") 

def getCoursesByCategory (request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text) 
    except:
        return HttpResponseNotFound("doğru düzgün bir kategori seç adam ol")
def getCoursesByCategoryId(request, category_id):
    category_list= list(data.keys())
    if(category_id> len(category_list)):
        return HttpResponseNotFound("adam gibi sayfa seç ")
    category_name = category_list[category_id -1]
    redirect_url =reverse('courses_by_category', args=[category_name])
    return redirect(redirect_url)
