from django.shortcuts import render, redirect
from . import forms, models 
from caruser.models import PlaceOrderModel
from django.contrib import messages
from django.urls import reverse_lazy 
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


# Create your views here.
class addCarBrandCreateView(CreateView):
    model = models.CarBrandModel
    form_class = forms.CarBrandForm
    template_name = 'add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Car Brand added successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Car Brand added failed!")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pageTitle"] = 'Add Car Brand'
        return context


class addCarDetailsCreateView(CreateView):
    model = models.CarModel
    form_class = forms.CarDetailsForm
    template_name = 'add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, "Car Details added successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "Car Details added failed!")
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pageTitle"] = 'Add Car Details'
        return context


class carDetailsView(DetailView):
    model = models.CarModel
    template_name = 'details.html'    
    pk_url_kwarg = 'id' 

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentsForm(data= self.request.POST)
        car = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car 
            new_comment.save() 
        return self.get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()  
        comment_form = forms.CommentsForm()


        context['car'] = car 
        context['comments'] = comments 
        context['comment_form'] = comment_form
        return context

    

def placeOrder(request, id):
    carOrdered = models.CarModel.objects.get(pk = id) 

    if carOrdered.quantity > 0:
        carOrdered.quantity -= 1
        carOrdered.save() 
    order = PlaceOrderModel.objects.create(car=carOrdered, carOwner=request.user)

    messages.success(request, "Car Ordered Successfully")
    return redirect('profile')
