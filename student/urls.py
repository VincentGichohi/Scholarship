from django.urls import path
from student.views import AboutView
urlpatterns = [
    path('index/', AboutView.as_view(), name='index')
]