from datetime import date, datetime
from django.shortcuts import get_object_or_404, redirect, render
from django.http import Http404, HttpResponseNotFound
from django.urls import reverse
from .models import Course, Category

data = {
    "programlama":"programlaam işine ait kurlar",
    "web":"web işine ait kurlar",
    "mobil":"mobil işine ait kurlar işine ait kurlar",
    "mobil-uygulama":"mobil işine ait kurlar işine ait kurlar",
}

db = {
    "courses": [
        {
          "title":"Javascript Kursu",
            "description":"Javascript Kurs Açıklaması",
            "imageUrl":"02.jpg",
            "slug":"java", 
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": True,
        },
        {
          "title":"Python Kursu",
            "description":"Python Kurs Açıklaması",
            "imageUrl":"03.jpg",
            "slug":"python", 
            "date": date(2022,8,10),
             "isActive": False,
             "isUpdated": True,
        },
        {
          "title":"Web Kursu",
            "description":"Web Kurs Açıklaması",
            "imageUrl":"04.jpg",
            "slug":"web", 
            "date": date(2022,7,10),
             "isActive": True,
             "isUpdated": False,
        },
    ],
    "categories":[
        {"id":1, "name":"programlama", "slug":"proglramlama"},
        {"id":2, "name":"web geliştirme", "slug":"web-gelistirme"},
        {"id":3, "name":"mobil uygulamalar", "slug":"mobil-uygulamalar"},
        ]
}

def index (request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    return render(request, "courses/index.html",{
        "categories": kategoriler,
        "courses" : kurslar
    })

def details (request, slug):
    course = get_object_or_404(Course, slug=slug)

    context = {'course': course}
    return render(request, 'courses/details.html', context) 

def getCoursesByCategory (request, category_name):
    try:
        category_text = data[category_name]
        return render(request, "courses/kurslar.html", {
            "category": category_name,
            "category_text": category_text
        })
    except:
        return HttpResponseNotFound("doğru düzgün bir kategori seç adam ol")
def getCoursesByCategoryId(request, category_id):
    category_list= list(data.keys())
    if(category_id> len(category_list)):
        return HttpResponseNotFound("adam gibi sayfa seç ")
    category_name = category_list[category_id -1]
    redirect_url =reverse('courses_by_category', args=[category_name])
    return redirect(redirect_url)
