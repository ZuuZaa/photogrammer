from django.urls import path, include
from customuser.views import (
    register_view,
    login_view,
    logout_view,
    profile_view,
    user_profile_view
)

urlpatterns = [
    path('api/', include('customuser.api.urls')),

    path('register', register_view, name="register"),
    path('login', login_view, name="login"),
    path('logout', logout_view, name="logout"),

    path('profile', profile_view, name="profile"),
    path('pfofile/<str:slug>', user_profile_view, name="user_profile")
]