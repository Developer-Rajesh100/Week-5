from .views import register, userLogin, userLogout, password_change_with_old_password
from django.urls import path

urlpatterns = [
    path('register/', register, name = 'register_page'),
    path('login/', userLogin, name = 'login'),
    path('logout/', userLogout, name = 'logout'),
    path('password_change', password_change_with_old_password, name = 'password_change_with_old_password')
]