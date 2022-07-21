from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    Res_id=models.IntegerField(primary_key=True)
    res_name=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='res_owner')

class Cat_Res(models.Model):
    cat_id=models.IntegerField(primary_key=True)
    cat_name=models.CharField(max_length=50)
    res=models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='res_cat')

class Iteams(models.Model):
    iteam_id=models.IntegerField(primary_key=True)
    iteam_name=models.CharField(max_length=50)
    cat=models.ForeignKey(Cat_Res,on_delete=models.CASCADE)
    price=models.FloatField()
    available=models.BooleanField(default=True)
    


