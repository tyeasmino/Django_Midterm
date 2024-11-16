from django.db import models 
from django.contrib.auth.models import User
from car.models import CarModel
# Create your models here.


class PlaceOrderModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.DO_NOTHING)
    carOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.carOwner} - {self.car.car_name}' 
    
