from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from users.forms import CreateUser, LoginForm


# ? home page
def index(request):
    return render(request, 'users/index.html')

# ? login page
def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username: str = form.cleaned_data['username']
            password: str = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('com-dashboard')
            form.add_error('', "Please enter correct username or password.")
    return render(request, 'users/login.html', {'login_form': form})

# ? register page
def register_user(request):
    form = CreateUser()
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    return render(request, 'users/register.html', {'register_form': form})

# ? logout page
@login_required(login_url='user-login')
def logout_user(request):
    logout(request)
    return redirect('index')