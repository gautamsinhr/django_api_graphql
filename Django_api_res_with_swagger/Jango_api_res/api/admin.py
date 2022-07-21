from django.contrib import admin
from .models import Restaurant,Cat_Res,Iteams

@admin.register(Restaurant)
class Restaurantadmin(admin.ModelAdmin):
    list_display=['Res_id','res_name','city','owner']
@admin.register(Cat_Res)
class Cat_res_admin(admin.ModelAdmin):
    list_display=['cat_id','cat_name','res']
@admin.register(Iteams)
class Iteamsadmin(admin.ModelAdmin):
    list_display=['iteam_id','iteam_name','cat','price','available']

