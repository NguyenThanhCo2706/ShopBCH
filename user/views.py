from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group, Permission
from .models import CustomerUser
from product.models import Product
from .forms import UserForm
# Create your views here.
class UserClass(LoginRequiredMixin ,View):
    login_url = '/user/login/'
    redirect_field_name = 'login-user'
    def get(self, request):
        if request.user.has_perm("user.view_user"):
            qs = CustomerUser.objects.all()
            return render(request, 'user/index.html', {'users': qs})
        else:
            qs = Product.objects.all()
            checkAdmin = request.user.is_superuser
            return redirect('/product/')
        # return render(request, 'user/login.html')


class CreateUser(View):
    def get(self, request):
        userForm = UserForm()
        return render(request, "user/create.html", {'userForm':userForm})
    def post(self, request):
        username =  request.POST.get('username')
        password = request.POST.get('password')
        avatar = request.FILES['avatar']
        # group = Group.objects.get(name = 'User')
        print(avatar)
        if avatar is None:
            avatar = "avatar.png"
        user = CustomerUser.objects.create(username=username, avatar=avatar)
        user.set_password(password)
        # user.groups.add(group)
        user.save()
        return redirect('/user/')

class DeleteUser(LoginRequiredMixin, View):
    login_url = '/user/login/'
    redirect_field_name = 'login-user'
    def post(self,request, id):
        if request.user.is_authenticated():
            user = CustomerUser.objects.get(id=id)
            user.delete()
            return redirect('/user/')

class UpdateUser(LoginRequiredMixin, View):
    login_url = '/user/login/'
    redirect_field_name = 'login-user'
    def get(self,request,id):
        user = CustomerUser.objects.get(id=id)
        f = UserForm(instance=user)
        return render(request, 'user/update.html', {'userForm': f,'user':user})
    def post(self,request,id):
        user = CustomerUser.objects.get(id=id)
        f = UserForm(request.POST, request.FILES ,instance=user)
        if f.is_valid():
            f.save()
            return redirect('/user/')           
        return HttpResponse('Invalid data update')     


class LoginUser(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'user/login.html')
    def post(self, request):
        username =  request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('/product/')
        else:       
            return HttpResponse('Invalid data login')
class LogoutUser(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/product/')

