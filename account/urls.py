from django.urls import path

from .views import (
    SignInView
)

app_name = 'account'

urlpatterns = [
    path('login', SignInView.as_view(), name='login')
]
