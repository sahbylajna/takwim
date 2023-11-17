# client_api/urls.py

from django.urls import path
from .views import ClientUserLogin,getClient,GetClientList,regesterClient

urlpatterns = [
    path('login/', ClientUserLogin.as_view(), name='client-user-login'),
    path('regester/', regesterClient.as_view(), name='client-user-regester'),
    path('getClient/', getClient.as_view(), name='client-get'),
    path('get-clients/', GetClientList.as_view(), name='get-client-list'),

]
