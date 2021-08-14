from django.urls import path
from account.api.views import (
    api_user_detail_view,
    api_users_view
    )

urlpatterns = [
    path('<int:id>', api_user_detail_view, name='user_detail'),
    path('', api_users_view, name='users')
]