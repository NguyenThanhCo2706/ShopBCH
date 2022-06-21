from .views import HomeView
from django.urls import path
app_name = 'Home'
urlpatterns = [
    path('',HomeView.as_view(), name='home' ),
]
