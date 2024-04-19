from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('submit/', views.submit_request, name='submit_request'),
    path('track/<int:request_id>/', views.track_request, name='track_request'),
    path('all/', views.all_requests, name='all_requests'),
    path('track/', views.track_request_by_id, name='track_request_by_id'),  
]
