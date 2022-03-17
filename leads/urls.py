from django.urls import path
from leads import views

app_name = 'leads'

urlpatterns = [
    path('main/', views.main_page, name='main')
    ]
