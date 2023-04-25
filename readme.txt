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
