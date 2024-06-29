from django.urls import path
from home.views import fetch_external_api_data, index

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('api/external-data/', fetch_external_api_data,
         name='fetch_external_api_data'),
]
