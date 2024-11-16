from django.urls import path
from . import views
urlpatterns = [ 
    path('addCarBrand/', views.addCarBrandCreateView.as_view(), name='addCarBrand'), 
    path('addCarDetails/', views.addCarDetailsCreateView.as_view(), name='addCarDetails'), 
    path('carDetails/<int:id>/', views.carDetailsView.as_view(), name='carDetails'), 


    path('placeOrder/<int:id>/', views.placeOrder, name='placeOrder'), 


    # path('edit/<int:id>/', views.updateInvestigationUpdateView.as_view(), name='edit_investigations'),  
    # path('delete/<int:id>/', views.deleteInvestigationDeleteView.as_view(), name='delete_investigations'), 
]