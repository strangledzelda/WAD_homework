from django.shortcuts import render, redirect
from .models import Deserts, Order, Drinks
from .forms import OrderForm


def home(request):
    deserts = Deserts.objects.all()
    return render(request, 'main/home.html', {'title': 'Главная страница', 'deserts': deserts})


def deserts(request):
    return render(request, 'main/deserts.html', {'title': 'Десерты'})


def drinks(request):
    return render(request, 'main/drinks.html', {'title': 'Напитки'})


def report(request):
    orders = Order.objects.all()
    return render(request, 'main/report.html', {'title': 'Отчёт', 'orders': orders})


def contact(request):
    return render(request, 'main/contact.html',{'title': 'Контакты'})


def add(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('home')
        else:
            error = 'Форма невалидна'
    form = OrderForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', context)
