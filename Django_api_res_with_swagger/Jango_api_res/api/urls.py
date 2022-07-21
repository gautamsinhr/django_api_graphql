from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API Doc",
      default_version='v1',
      description="Restaurants",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@manohar.borana"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
   path('apioverview/',views.Apioverview.as_view(),name='api-overview'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
   path('res_data_id/<int:id>',views.ResDataWithID.as_view(),name='data_with_id'),
   path('res_data/',views.RestData.as_view(),name='all-data'),
   path('cat_data_id/<int:id>',views.CatDataWithId.as_view(),name='cat_data_with_id'),
   path('cat_data/',views.CatData.as_view(),name='cat-all-data'),
   path('iteam_data_id/<int:id>',views.IteamWithID.as_view(),name='iteam_data_with_id'),
   path('iteam_data/',views.IteamData.as_view(),name='iteam-all-data'),
]