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
    path('ministries/<int:ministry_id>/add_photo/', views.add_photo, name='add_photo'),
    path('ministries/<int:ministry_id>/assoc_member/<int:member_id>/', views.assoc_member, name='assoc_member'),
    path('events/', views.events_index, name='events_index'),
    path('events/create/', views.EventCreate.as_view(), name='events_create'),
    path('events/<int:event_id>/', views.events_detail, name='events_detail'),
    path('events/<int:pk>/update/', views.EventUpdate.as_view(), name='events_update'),
    path('events/<int:pk>/delete/', views.EventDelete.as_view(), name='events_delete'),
    path('members/', views.members_index, name='members_index'),
    path('members/create/', views.MemberCreate.as_view(), name='members_create'),
    path('members/<int:member_id>/', views.members_detail, name='members_detail'),
    path('members/<int:pk>/update/', views.MemberUpdate.as_view(), name='members_update'),
    path('members/<int:pk>/delete/', views.MemberDelete.as_view(), name='members_delete'),
]