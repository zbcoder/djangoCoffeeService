from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.


def login(request):
    return render(request, 'profile/login.html')


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользовать {username} был успешно создан!')
            return redirect('login')
    else:
        form = NewUserForm()
    return render(
        request, "registration/register.html",
        {'title': 'Регистрация',
        'form': form}
    )