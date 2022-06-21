from django.urls import path,include
from . import views

app_name = 'User'

urlpatterns = [
    path('', views.UserClass.as_view(), name='users'),
    path('create/', views.CreateUser.as_view(), name='create-user'),
    path('add/', views.CreateUser.as_view(), name='add-user'),
    path('delete/<int:id>/', views.DeleteUser.as_view(), name='delete-user'),
    path('update/<int:id>/', views.UpdateUser.as_view(), name='update-user'),
    path('updateProductData/<int:id>/', views.UpdateUser.as_view(), name='update-user-post'),
    path('login/', views.LoginUser.as_view(), name='login-user'),
    path('logout/', views.LogoutUser.as_view(), name='logout-user'),
]