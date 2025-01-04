from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='shorten'), #homepage
    path('<str:short_code>/', views.redirect_url, name='redirect')  # redirect
]
