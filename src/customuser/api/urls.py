from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from customuser.api.views import (
    api_user_detail_view,
    api_users_view
    )

urlpatterns = [
    path('<int:id>', api_user_detail_view, name='user_detail'),
    path('', api_users_view, name='users'),
    path('login', obtain_auth_token, name='login'),
]