from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', views.CarUserRegistrationCreateView.as_view(), name="signup"),
    path('signin/', views.CarUserLoginCreateView.as_view(), name="signin"),
    path('signout/', views.CarUserLogoutCreateView.as_view(), name="signout"),
    path('profile/', views.CarUserProfileCreateView.as_view(), name="profile"),
    path('edit_profile/', views.CarUserEditProfile.as_view(), name="edit_profile"),
    path('update_pass/', views.update_pass, name="update_pass"),
]
