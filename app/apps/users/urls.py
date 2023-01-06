from django.urls import path

from .views import LoginView, LogoutView, SignUpView, UserView

app_name = 'apps.users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/', UserView.as_view(), name='user'),
]
