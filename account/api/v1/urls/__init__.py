from django.urls import path,include

urlpatterns = [
    path('',include('account.api.v1.urls.account')),
    path('profile/',include('account.api.v1.urls.profiles')),
]