from django.contrib import admin
from .models import CarBrandModel, CarModel, CommentModel


# Register your models here.
class CarBrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name', )}
    list_display = ['name', 'slug'] 

admin.site.register(CarBrandModel, CarBrandAdmin)
admin.site.register(CarModel) 
admin.site.register(CommentModel) 