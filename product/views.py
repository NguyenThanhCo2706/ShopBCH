import re
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from numpy import product

from user.models import CustomerUser
from .serializers import ProductSerializer
from .forms import ProductForm, CategoryForm, VariationFrom
from .models import Product, Category, Variation, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from order.models import Order, OrderDetail

class ProductClass(View):
    def get(self, request):
        numberOrder = 0
        if request.user.is_authenticated:
            id = request.user.id
            numberOrder = Order.objects.filter(user=id, is_completed = False).count()
        if 'cart' not in request.session:
            request.session['cart'] = {}
        qs1 = Category.objects.values("id", "title")
        qs = Product.objects.all()
        checkAdmin = request.user.is_superuser
        return render(request, 'product/index.html', {'numberOrder': numberOrder,'products': qs,'category_title': qs1, 'checkAdmin': checkAdmin, "cart": len(request.session['cart'])})

class CreateProduct(View):
    def get(self, request):
        productForm = ProductForm()
        checkAdmin = request.user.is_superuser
        if request.user.has_perm("product.add_product"):
            return render(request, "product/create.html", {'productForm':productForm, 'checkAdmin': checkAdmin})
    def post(self, request):
        product = ProductForm(request.POST, request.FILES)
        if request.user.is_authenticated:
            if request.user.has_perm("product.add_product"):
                if product.is_valid():
                    product.save()
                    return redirect('/product/')
                else:
                    return HttpResponse('Invalid data input')


class DeleteProduct(View):
    def post(self,request, id):
        product = Product.objects.get(id=id)
        product.delete()
        return redirect('/product/')

class UpdateProduct(View):
    def get(self,request,id):
        product = Product.objects.get(id=id)
        checkAdmin = request.user.is_superuser
        f = ProductForm(instance=product)
        return render(request, 'product/update.html', {'productForm': f,'product':product, 'checkAdmin': checkAdmin})
    def post(self,request,id):
        product = Product.objects.get(id=id)
        f =ProductForm(request.POST, request.FILES,instance=product)
        if f.is_valid():
            f.save()
            return redirect('/product/')           
        return HttpResponse('Invalid data update')

class DetailProduct(View):
    def get(self,request,id):
        if 'cart' not in request.session:
            request.session['cart'] = {}

        numberOrder = 0
        if request.user.is_authenticated:
            iduser = request.user.id
            numberOrder = Order.objects.filter(user=iduser, is_completed = False).count()
        product = Product.objects.get(id=id)
        messages = Message.objects.filter(product=product)
        print(messages)
        qs1 = Category.objects.values("id", "title")
        checkAdmin = request.user.is_superuser
        if request.user.username:
            avatar = CustomerUser.objects.get(username=request.user.username).avatar.url            
        else:
            avatar = 'aaa'
        return render(request, 'product/detail.html', {'numberOrder': numberOrder,'product':product, 'cart': len(request.session['cart']), 'category_title': qs1, 'checkAdmin': checkAdmin, 'messages': messages, 'avatar': avatar})

def category_search(request, id):
    if 'cart' not in request.session:
            request.session['cart'] = {}
    numberOrder = 0
    if request.user.is_authenticated:
        id = request.user.id
        numberOrder = Order.objects.filter(user=id, is_completed = False).count()
    product = Product.objects.filter(category = id)
    qs1 = Category.objects.values("id", "title")
    checkAdmin = request.user.is_superuser
    return render(request, 'product/index.html', {'numberOrder': numberOrder,'products': product, "cart": len(request.session['cart']), 'category_title': qs1, 'checkAdmin': checkAdmin})

class CategoryClass(View):
    def get(self, request):
        if 'cart' not in request.session:
            request.session['cart'] = {}
        numberOrder = 0
        if request.user.is_authenticated:
            id = request.user.id
            numberOrder = Order.objects.filter(user=id, is_completed = False).count()
        qs = Category.objects.all()
        qs1 = Category.objects.values("id", "title")
        checkAdmin = request.user.is_superuser
        return render(request, 'category/index.html', {'numberOrder': numberOrder,'categoryes': qs, "cart": len(request.session['cart']), 'category_title':qs1, 'checkAdmin': checkAdmin})
class CreateCategory(View):
    def get(self, request):
        categoryForm = CategoryForm()
        checkAdmin = request.user.is_superuser
        return render(request, "category/create.html", {'categoryForm':categoryForm, 'checkAdmin': checkAdmin})
    def post(self, request):
        category = CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            return redirect('/product/category/')
        else:
            return HttpResponse('Invalid data input')

class DeleteCategory(View):
    def get(self,request, id):
        category = Category.objects.get(id=id)
        category.delete()
        return redirect('/product/category/')
class UpdateCategory(View):
    def get(self,request,id):
        category = Category.objects.get(id=id)
        f = CategoryForm(instance=category)
        checkAdmin = request.user.is_superuser
        return render(request, 'category/update.html', {'categoryForm': f,'category':category, 'checkAdmin': checkAdmin})
    def post(self,request,id):
        category = Category.objects.get(id=id)
        f = CategoryForm(request.POST,instance=category)
        if f.is_valid():
            f.save()
            return redirect('/product/category/')           
        return HttpResponse('Invalid data update')





class VariationClass(View):
    def get(self, request):
        varis = Variation.objects.all()
        checkAdmin = request.user.is_superuser
        return render(request, 'variation/index.html', {'variations': varis, 'checkAdmin': checkAdmin})

class CreateVariation(View):
    def get(self, request):
        checkAdmin = request.user.is_superuser
        variationForm = VariationFrom()
        return render(request, "variation/create.html", {'variation':variationForm, 'checkAdmin': checkAdmin})
    def post(self, request):
        variation = VariationFrom(request.POST)
        if variation.is_valid():
            variation.save()
            return redirect('/product/variation/')
        else:
            return HttpResponse('Invalid data input')

class DeleteVariation(View):
    def get(self, request, id):
        varia = Variation.objects.get(id=id)
        varia.delete()
        return redirect('/product/variation/')

class UpdateVariation(View):
    def get(self,request,id):
        varia = Variation.objects.get(id=id)
        form = VariationFrom(instance=varia)
        return render(request, 'variation/update.html', {'variationForm': form, 'variation': varia})
    def post(self,request,id):
        variation = Variation.objects.get(id=id)
        form = VariationFrom(request.POST,instance=variation)
        if form.is_valid():
            form.save()
            return redirect('/product/variation/')           
        return HttpResponse('Invalid data update')


def AddCart(request, id):
    id = str(id)
    product = Product.objects.get(id=id)
    if id in request.session['cart'].keys():
        itemCart = {
            "id": id, 
            "name": product.title,
            "price": product.price,
            "image": product.image_view.url,
            "number" : int(request.session['cart'][id]['number'] + 1),
            "total": float(product.price * int(request.session['cart'][id]['number'] + 1) ),
            
        }
    else:
        itemCart = {
            "id" : id,
            "name": product.title,
            "price": product.price,
            "image": product.image_view.url,
            "total": product.price,
            "number" : 1
        }
    request.session['cart'][id] = itemCart
    request.session.modified = True
    return redirect('/product/')

from order.forms import OrderForm
def Cart(request):
    form = OrderForm()
    qs1 = Category.objects.values("id", "title")
    if 'cart' not in request.session:
        request.session['cart'] = {}
    numberOrder = 0
    if request.user.is_authenticated:
        id = request.user.id
        numberOrder = Order.objects.filter(user=id, is_completed = False).count()
    return render(request, 'product/cart.html', {'numberOrder':numberOrder, 'cartInfo':request.session['cart'],'category_title':qs1, 'cart': len(request.session['cart']), "form":form})
def DeleteCart(request, id):
    id=str(id)
    request.session['cart'].pop(id)
    request.session.modified = True
    return redirect('/product/cart/')

class SearchProduct(View):
    def get(self, request, name):
        qs = Product.objects.filter(title__icontains=name)
        data = ProductSerializer(qs, many=True)
        return JsonResponse(data.data, safe=False, status=200)

class CreateMessage(View):
    def post(self, request):
        id_product = request.POST.get('id_product')
        id_user = request.user.id
        message = request.POST.get('message')
        product = Product.objects.get(id=id_product)
        user = CustomerUser.objects.get(id=id_user)
        Message.objects.create(product=product, user=user, message=message)
        return redirect('/product/detail/'+str(id_product)+'/')