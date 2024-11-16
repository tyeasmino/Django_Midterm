from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),    
    path('brand/<slug:car_slug>/', views.home, name='brand_wise_cars'),  
    path('caruser/', include('caruser.urls')),
    path('car/', include('car.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
