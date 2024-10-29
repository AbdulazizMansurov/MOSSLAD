from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .forms import *
from .models import *


#
# Create your views here.

class Products_list(ListView):
    model = Products
    context_object_name = 'products'
    template_name = 'store/products_list.html'

    extra_context = {
        'title': "Кондитерские изделия"
    }
    categories = Category.objects.all()
    extra_context['categories'] = categories

class Products_list_4(Products_list):
    template_name = 'store/products_list_4.html'

class Product_detail(DetailView):
    model = Products
    context_object_name = 'products'

    template_name = 'store/product_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = Products.objects.get(pk=self.kwargs['pk'])
        context['title'] = product.title
        context['product'] = product

        return context

class ProductsListByCategory(Products_list):
    def get_queryset(self):
        return Products.objects.filter(category_id=self.kwargs['pk'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListByCategory, self).get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context






def about(request):
    return render(request, 'store/about.html', context=None)

@login_required
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    context = {
        'title': 'Ваш профиль',
        'user': user,
    }
    return render(request, 'store/profile.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно прошли авторизацию!')
            next = request.POST.get('next', 'index')
            return redirect(next)
    else:
        form = LoginForm()
    context = {
        'form': form,
        'title': 'Login | Mosslad'
    }
    return render(request, 'store/user_login.html', context)


def user_logout(request):
    logout(request)
    messages.warning(request, "Вы вышли из своего аккаунта!")
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт успешно открыт!')
            return redirect('login')
    else:
        form = RegistrationForm()
    context = {
        'form': form,
        'title': 'Registartion | Mosslad'
    }
    return render(request, 'store/register.html', context)