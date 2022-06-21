from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, OrderDetail
from .forms import OrderForm, OrderDetailForm
from django.views import View
from product.models import Product, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
def getTotal(cart):
    s = 0
    for key, value in cart.items():
        s += cart[key]['total']
    return s
@login_required(login_url='/user/login/')
def CreateOrder(request):
    temp_cart = request.session['cart']
    if request.method == "POST":
        name = request.POST["name_receive"]
        phone = request.POST["phone_number"]
        user = request.user.id
        add = request.POST["address_receive"]
        des = request.POST["description"]
        total = getTotal(temp_cart)
        order = Order(user = user, phone_number = phone, shipping_address = add, order_description = des, name_receive = name, total_price = total)
        order.save()
        for key, value in temp_cart.items():
            orderDetail = OrderDetail(order_id= order.id, pro_name = temp_cart[key]['name'], amount = temp_cart[key]['number'], address_delivery = add,money = temp_cart[key]['price'], total_money = temp_cart[key]['total'])
            orderDetail.save()
        del request.session['cart']
        request.session.modified = True
        return redirect('/product/')
    else:
        return HttpResponse('Invalid data input')
class CreateOrderAll(LoginRequiredMixin, View):
    login_url = '/user/login/'
    def get(self, request):
        if request.user.is_superuser:
            order = Order.objects.all()
        else:
            id = request.user.id
            order = Order.objects.filter(user=id)
        if 'cart' not in request.session:
            request.session['cart'] = {}
        qs1 = Category.objects.values("id", "title")
        qs = Product.objects.all()
        checkAdmin = request.user.is_superuser
        numberOrder = 0
        if request.user.is_authenticated:
            id = request.user.id
            numberOrder = Order.objects.filter(user=id, is_completed = False).count()
        return render(request, 'order/order.html', { "numberOrder": numberOrder,'products': qs,'category_title': qs1, 'checkAdmin': checkAdmin, "cart": len(request.session['cart']), 'order': order, "number_order": len(order)})

class GetOrderDetail(LoginRequiredMixin, View):
    login_url = '/user/login/'
    def get(self, request, id):
        order = OrderDetail.objects.all()
        buy = Order.objects.get(id=id)
        if 'cart' not in request.session:
            request.session['cart'] = {}
        qs1 = Category.objects.values("id", "title")
        qs = Product.objects.all()
        checkAdmin = request.user.is_superuser
        order_detail = []
        for item in order:
            if id == item.order_id:
                order_detail.append(item)
        numberOrder = 0
        if request.user.is_authenticated:
            id = request.user.id
            numberOrder = Order.objects.filter(user=id, is_completed = False).count()
        return render(request, 'order/order-detail.html', { "numberOrder": numberOrder, 'products': qs,'category_title': qs1, 'checkAdmin': checkAdmin, "cart": len(request.session['cart']), 'order_detail': order_detail, "buy": buy.is_delivered})

def ConfirmOrder(request, id):
    order = Order.objects.get(id = id)
    order.is_delivered = True
    order.save()
    return redirect('/order/all-order/')
def DeleteOrderDetail(request, id):
    orderDetail = OrderDetail.objects.get(id = id)
    key = orderDetail.order_id
    orderDetail.delete()
    objects = OrderDetail.objects.filter(order_id = key)
    count = 0
    for item in objects:
        count += item.total_money
    if count == 0:
        Order.objects.get(id = key).delete()
    else:
        Order.objects.filter(id = key).update(total_price=count)
    return redirect('/order/all-order/')
def OrderComplete(request, id):
    order = Order.objects.get(id = id)
    order.is_completed = True
    order.save()
    return redirect('/order/all-order/')
