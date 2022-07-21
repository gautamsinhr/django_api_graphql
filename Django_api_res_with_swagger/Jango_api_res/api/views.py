from rest_framework.generics import GenericAPIView
from .models import Restaurant,Cat_Res,Iteams
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer,Cat_resSerializer, RestaurantSerializer,IteamSSerializer




class Apioverview(GenericAPIView):
    permission_classes = (IsAuthenticated,)   
    def get(self, request):
        api_urls={
        "For Access Token":"api-token-auth/",
        'Restaurant List':'res_data/',
        'Restaurant List By Single ID':'res_data_id/<int:id>',
        'Category List':'cat_data/',
        'Category List by single ID':'cat_data_id/<int:id>',
        'Iteams List':'iteam_data/',
        'Iteam by Particular ID':'iteam_data_id/<int:id>',

    }   
        return Response(api_urls)


class ResDataWithID(GenericAPIView):
    
    permission_classes = (IsAuthenticated,)  
    serializer_class=RestaurantSerializer  
    def get(self,request,id):
        res=Restaurant.objects.get(Res_id=id)
        user_res=UserSerializer(res.owner,many=False)
        serializer=RestaurantSerializer(res)
        return Response({"Restaurant":serializer.data,"Owner":user_res.data})
     
    def put(self,request,id):
            res=Restaurant.objects.get(Res_id=id)
            serializer=RestaurantSerializer(res,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Data Updated'})
            return(serializer.errors)
      
    def delete(self,request,id):
            res=Restaurant.objects.get(Res_id=id)
            res.delete()
            return Response({'msg':'Data Deleted'})

class RestData(GenericAPIView):
    serializer_class=RestaurantSerializer
    permission_classes = (IsAuthenticated,)    
    def get(self,request):
        res=Restaurant.objects.all()
        serializer=RestaurantSerializer(res,many=True)
        return Response(serializer.data)
          
    def post(self,request):
        serializer=RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Inserted'})
        return(serializer.errors)
    
class CatData(GenericAPIView):
    serializer_class=Cat_resSerializer
    permission_classes = (IsAuthenticated,)    
    def get(self,request):
        cat=Cat_Res.objects.all()
        serializer=Cat_resSerializer(cat,many=True)
        return Response(serializer.data)
     
    def post(self,request):    
        serializer=Cat_resSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Inserted'})
        return(serializer.errors)

class CatDataWithId(GenericAPIView):
    serializer_class=Cat_resSerializer
    permission_classes = (IsAuthenticated,)    
    def get(self,request,id):
        cat=Cat_Res.objects.get(cat_id=id)
        serializer=Cat_resSerializer(cat)
        res=RestaurantSerializer(cat.res,many=False)
        return Response({'category':serializer.data,'Restaurant':res.data})
       
    def put(self,request,id):
        cat=Cat_Res.objects.get(cat_id=id)
        serializer=Cat_resSerializer(cat,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return(serializer.errors)
       
    def delete(self,request,id):
        cat=Cat_Res.objects.get(cat_id=id)
        cat.delete()
        return Response({'msg':'Data Deleted'})

class IteamData(GenericAPIView):
    serializer_class=IteamSSerializer
    permission_classes = (IsAuthenticated,)    
    def get(self,request):
        iteam=Iteams.objects.all()
        serializer=IteamSSerializer(iteam,many=True)
        return Response(serializer.data)
       
    def post(self,request):
        serializer=IteamSSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Inserted'})
        return(serializer.errors)

class IteamWithID(GenericAPIView):
    serializer_class=IteamSSerializer
    permission_classes = (IsAuthenticated,)    
    def get(self,request,id):
        iteam=Iteams.objects.get(iteam_id=id)
        user_res=UserSerializer(iteam.cat.res.owner,many=False)
        res=RestaurantSerializer(iteam.cat.res,many=False)
        cat = Cat_resSerializer(iteam.cat,many=False)
        serializer=IteamSSerializer(iteam)
        return Response({'item':serializer.data,'category':cat.data,'restaurant':res.data,"Owner":user_res.data})
    
    def put(self,request,id):
        iteam=Iteams.objects.get(iteam_id=id)
        serializer=IteamSSerializer(iteam,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return(serializer.errors)
       
    def delete(self,request,id):
        iteam=Iteams.objects.get(iteam_id=id)
        iteam.delete()
        return Response({'msg':'Data Deleted'})


    

       
