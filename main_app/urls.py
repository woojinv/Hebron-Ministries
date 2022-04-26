from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('ministries/', views.ministries_index, name='index'),
    path('ministries/<int:ministry_id>/', views.ministries_detail, name='detail'),
    path('ministries/create/', views.MinistryCreate.as_view(), name='ministries_create'),
    path('ministries/<int:pk>/update/', views.MinistryUpdate.as_view(), name='ministries_update'),
    path('ministries/<int:pk>/delete/', views.MinistryDelete.as_view(), name='ministries_delete'),
    path('ministries/<int:ministry_id>/add_event/', views.add_event, name='add_event'),
    path('members/create/', views.MemberCreate.as_view(), name='members_create')
]