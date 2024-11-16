from django.shortcuts import render
from car.models import CarBrandModel, CarModel


def home(request, car_slug = None):
    carBrand = CarBrandModel.objects.all()
    car = CarModel.objects.all()

    if car_slug is not None:
        brand = CarBrandModel.objects.get(slug = car_slug)
        car = CarModel.objects.filter(brand = brand)


    return render(request, 'index.html', {'carBrand' : carBrand, 'car': car})

