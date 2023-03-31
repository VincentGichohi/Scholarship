from operator import imod
from django.urls import path, include
from knox import views as knox_views
from .views import SignInAPI, SignUpAPI, MainUser

urlpatterns = [
    path('api/auth/', include('knox.urls')),
    path('api/auth/signup/', SignUpAPI.as_view(), name='register'),
    path('api/auth/login/', SignInAPI.as_view(), name='login'),
    path('api/auth/user/', MainUser.as_view(), name='user'),
    path('api/auth/logout/', knox_views.LogoutView.as_view(), name='knox-logout'),
    # path('gmail/login/', GmailLoginView.as_view(), name='gmail_login'),
]
