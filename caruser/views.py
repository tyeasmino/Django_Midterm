from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms, models
from django.contrib import messages

from django.contrib.auth import update_session_auth_hash 
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView 



# Create your views here.
class CarUserRegistrationCreateView(CreateView):
    model = User
    form_class = forms.CarUserRegistrationForm
    template_name = "user_registration_login.html"
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Account created successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Provide correct information to sign up")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pageTitle"] = 'Sign Up'
        return context
    
    
class CarUserLoginCreateView(LoginView):
    template_name = 'user_registration_login.html'    

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, "Sign in successful!!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Sign in information is incorrect!")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pageTitle"] = 'Sign In'
        return context


class CarUserLogoutCreateView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('signin')


@method_decorator(login_required, name='dispatch')
class CarUserProfileCreateView(CreateView):
    model = models.PlaceOrderModel
    form_class = forms.CarUserUpdateInfofForm
    template_name = 'user_profile.html'

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['user_ordered'] = models.PlaceOrderModel.objects.filter(carOwner=self.request.user) 
        return context
 
 
@method_decorator(login_required, name='dispatch')
class CarUserEditProfile(UpdateView):
    model = User
    form_class = forms.CarUserUpdateInfofForm
    template_name = 'user_profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset = None):
        return self.request.user 
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pageTitle"] = 'update'
        return context

 

@login_required
def update_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, "Password updated successfully!!")
                return redirect('profile')
            
        else:
            form = PasswordChangeForm(user=request.user)
        
        return render(request, 'passchange.html', {'form' : form}) 
    else:
        return redirect('signin')
