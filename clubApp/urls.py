from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('clubs/', views.clubs_view, name='clubs'),
    path('events/', views.events_view, name='events'),
    path('announcements/', views.announcements_view, name='announcements'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('club/<int:id>/', views.club_detail_view, name='club_detail'),
    path('club/<int:id>/join/', views.join_club_view, name='join_club'),
    path('event/<int:id>/register/', views.register_event_view, name='register_event'),
]
