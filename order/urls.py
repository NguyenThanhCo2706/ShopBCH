from django.urls import path,include
from . import views

app_name = 'Order'
urlpatterns =[
    path("new-order/", views.CreateOrder, name="new-order"),
    path("all-order/", views.CreateOrderAll.as_view(), name="all-order"),
    path("confirm-order/<int:id>/", views.ConfirmOrder, name="confirm-order"),
    path("order-detail/<int:id>/", views.GetOrderDetail.as_view(), name="order-detail"),
    path("delete-order-detail/<int:id>/", views.DeleteOrderDetail, name="delete-order-detail"),
    path("order-complete/<int:id>/", views.OrderComplete, name="order-complete"),
]