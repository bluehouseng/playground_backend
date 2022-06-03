from django.urls import path 
from .views import get_user_list, get_user_detail, active_users

app_name = 'account'

urlpatterns = [ 
    path('', get_user_list, name="user_lists"),
    path('user/<int:pk>/', get_user_detail, name="user_details"),
    path('user/active/', active_users, name="active_users"),
]