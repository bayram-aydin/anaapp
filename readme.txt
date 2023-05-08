ana dizini ekledikten sonra projeyi çalıştırmak için:
"python manage.py runserver"
çalışan projeyi durdurma:
"ctrl + C"
projenin bölümlerini oluşturmak için içine uygulama indirmek gerekiyor.
uygulama oluşturmak için:
"python manage.py startapp courses"
proje ile ilgili genel ayarlar anaapp içindeki "settings.py" dir.
yeni eklediğin uygulamayı projeye bağlamak için:
settings.py sayfasına git. 
"INSTALLED_APPS =" bölümünü bul.
en altına yeni uygulamaya verdiğin adı ekle.
yeni uygulamaya url yapısı ekleyeceksen uygulama içine "urls.py" sayfası ekle.
sayfanın en üstüne kullanıcak modülleri ekle örneğin:
"from django.urls import path" ve from django.http import HttpResponse"
ondan sonra altına fonksiyon yapısını kur.
ondan sonra "urlpatterns = [" url yapısını kur.
şimdi
yeni uygulamaya eklediğin urls sayfasını ana uygulamadaki "urls.py" dosyasına tanıt:
" path('', include('courses.urls'))," 
hoca fikir değiştirdi.
fonksiyon yapısını aldı aynı dizinde bulunan "views.py" dosyasına geçirdi.
bu sefer fonksiyonların olduğu "views.py" sayfasını 
aynı dizindeki "urls.py" ye göstermek gerekiyor. 
onu da:
"from . import views" şeklinde "urls.py" sayfasının üst kısmına yazarsın.
artık "views" e ulaştın. views teki fonksiyonları başına "views." yazarak kullanabilirsin.
video 2.3 te kaldık. bunda git ve github bağlantısı yapacak.
git kuruldu. github bağlantısı yapıldı.
projeye bir tane git.md dosyası ekledim. git ile ilgili bilgileri oraya yazdım.
video 2.4 te url yapısını pekiştirmek için uygulama yaptı.
projeye yeni bir modül ekledik adı pages sırasıyla
yeni modülü anaapp altındaki seetings.py de INSTALLED_APPS altına tanıttık.
sonra pages içine urls.py sayfası ekledik. 
tüm projeye bakan url bağlantılarını buraya aldık.
Önemli: anaapp altındaki urls.py sayfasında "urlpatterns" altında uygulamalara eklenen
 urls.py sayfalarını eklemek gerekiyor.
 yeni eklenen pages altında urls.py de eklenilen url lerin çalışması için aynı dizindeki
 views.py sayfasına fonksiyonları yazmak ve sayfanın en üstünde 
 sayfalar arası bağlantıları kurmak gerekiyor.
 dinami kurl tanımlarken url yoluna "'<category>'"şeklinde yazılır ve
 views.py de fonksiyon lar tanımlanırken "request"in yanına 
 (request, category): bu şekilde ikinci bir parametre vermek gerekiyor.
 not: dinamik url yazdığında her zaman en altta olması gerekir.
 yoksa üsttekilerin çalışmasını engeller.
 video 2.6 ya geldik bitti. 2.7 deyiz.
 url redirect bişey anlatıldı. url nin yeniden yönlendirilmesi ile ilgili.
 video 2.8 from django.urls import reverse metodu ve args diye bir metod kullandık.
 url lere isim vererek değişiklik gerektiğinde tek merkezden tüm sayfaları gezmeden
 değiştirme imkanı veriri.
 urls & views dersleri bitti
 video 3.3 te kaldık.
 ana dizine klasör eklersen settins.py ye gidip
 TEMPLATES altında bulunan bölüme gidip "BASE_DIR / "templates","
 buşekilde ekleme yapılır.
 3.13 videoda uygulama altına static klasörü ekleyip resimleri bağladık.
 1- uygulama altındaki 'static' klasörü anaapp teki STATIC_URL = 'static/'
 eklenmiş olmalı.
 2- uygulama altına satatic klasörü onun altına tekrar bir klasör ekledik courses adında
 yani hangi uyguladaysak onun adını verdik.
 ondan sonra css, js, img klasörlerini içine attık. (anaapp\courses\static\courses\img)
 3- views içindeki data kaynağında veya database de resmin url yolu yazılmayacak
 sadece klasör içindeki adı doğru yazılacak:("imageUrl":"02.jpg",)
 4-resmin çağırıldığı html sayfasında url yolu sağlanacak. mesela:
  <img src="{% static 'courses/img/'|add:course.imageUrl %}">
  önemli: pip işaretinden sonra "|" boşluk bırakırsan url yolu bozuluyor ve resmi göremiyor.
  bir dosyaya
  {% extends 'layout.html' %}
{% load static %}
ikisini birlikte çağırısan extends i aşağıya yazarsan hata veriyor.
 en üste yazılmasını istiyor.
 global seviyede static kalsörü ekleme işlemleri.
 ana dizindeki seetings sayfasına STATICFILES_DIRS = [
    BASE_DIR / "static",
]
kodunu ekle.
ana dizinde ana çatıyı kuran htmtl sayfasına git.(layout.html)
en üste {% load static %} işlemini yap ondan sonra
<link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
bağlantısını kur.
4. bölüm: MODELS
models denene şey veri tabanında oluştutulan tabloların adları.
model ekleme:
projeye eklenen modüllerin altında models.py dosyası var.
bu dosyaya modelleri oluşturuyoruz.
mesela: from django.db import models
        class Course(models.Model):
        title = models.CharField(max_length=50)
models ten çok seçenek çağırılabilir. django da field lar geniş bir konu 
sitesinden inceleme yapılmalı. 
video 4.3 migrations 
python manage.py migrate
komutu ile migrations yapıldı. db browser indirildi.
yeni migrations oluşturma: python manage.py makemigrations
komutunu çalıştırdık ardından courses uygulaması altında 
migrations klasörü içinde 0001_inintial.py adında bir sayfa oluşturuldu.
ama bunu da ayrıca uygulamak gerekiyor.
migrations uygulama:  python manage.py migrate
çalıştırdık ve uygulandı.
veri tabanına veri ekleme işlemleri:
internette django queries arattır.
django documantationdan yararlan.
shell moduna geçiş : python manage.py shell
shell moduna çıkış : ctrl + z + enter
DÖRDÜNCÜ BÖLÜM:
Yönetim Paneli:
django admin aratıp, djangoproject.com da django sdmin site bölümünü inceleme
yönetim paneline giriş url/admin yaz panele geldik.
consola gel
python manage.py createsuperuser
çalıştır. kullanıcı adını soracak. istersen değiştir. admin yaz.
sonra mail adresi gir. parola isteyecek.
kullanıcı ad: bayram
e-posta : bayram@bayram.com
password : 963852741

kullanıcı ad: zeynep
e-posta : zeynep@zeynep.com
password : Hastane...1

ilk açıldığında panelde yönetici tanımlama seçeneği oluyor.
sitedeki modelleri yönetim paneline tanımlama:
courses altında bulunan admin.py sayfasına aşağıdaki kodları çalıştırısan
yönetim paneline bu modülü tanıtır.
from django.contrib import admin
from .models import Course
admin.site.register(Course)

admin panelini şekillendirme işlemi:
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=("title","isActive","slug")

bir alanı sadece okunabilen bir alan yapmak için: readonly_fields=("slug")
mesela arama penceresi için:  search_fields=("title","description")
sonuç olarak seçenek çok.
django dokümanlarını inceleyerek detay öğrenmek lazım.

veri tablolarını models.py içinde class olarak tanımladık.
ondan sonra admin.py içinde bu clas lara özellikler veriyoruz.
yani yönetim panelinde alacakları davranış şeklini bu sayfada veriyoruz.

video 6.1 de models.py içinde var olan course klasına category sütunu ekledik.
direk migrate edersek hata verir. iki seçenek var. db dosyasını silip baştan migrate etmek veya
defult değeri girmek yani:  
category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
amacımız kategoriler ile bağlantı kurmak.
ondan sonra: python manage.py makemigrations
ondan sonra: python manage.py migrate  
böyle olunca sorun çıkmadı.  
klavye çalıştı.

PAGİNATİON diye bişey var.
hem boostrap ta hem djangoda açıklaması var.
bir sayfaya kaç tane kurs göstersin anlamında bir sayfalama şekli.


