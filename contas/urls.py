from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page),
    path('cadastro/', views.cadastro_page)
]