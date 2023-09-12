from django.urls import path

from user.views import register, login, logout_view



urlpatterns = [

    path('register', register, name='register'),

    path('login', login, name='login'),

    path('logout', logout_view, name='logout'),

]