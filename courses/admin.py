from django.contrib import admin
from .models import Course, Category

# Register your models here.
#admin.site.register(Course)
#admin.site.register(Category)
# admin paneline yansımayı ayarlamak için aşağıdaki şekilde yazıldı.
# bir alanı sadece okunabilir bir alana çevirmek için: readonly_fields=("slug")
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=("title","isActive","slug")
    list_display_links=("title","slug")
    readonly_fields=("slug",)
    list_editable=("isActive",)
    search_fields=("title","description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("name","slug")
    list_display_links=("name","slug")
    



