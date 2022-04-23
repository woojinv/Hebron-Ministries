from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ministries/', views.ministries_index, name='index'),
    path('ministries/<int:ministry_id>/', views.ministries_detail, name='detail'),
    path('ministries/create/', views.MinistryCreate.as_view(), name='ministries_create'),
]