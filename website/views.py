from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from website.models import reviews,products

from django.contrib.auth.forms import UserCreationForm
def home(request):

    review = reviews.objects.all()

    return render(request, 'index.html', {'user': request.user, 'review': review })

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        action = request.POST.get('action')  # Determine if it's login or registration

        if action == 'login':
            # Handle login
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not username or not password:
                messages.error(request, 'Please provide both username and password.')
                return render(request, 'login.html')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, 'Invalid username or password.')
                return render(request, 'login.html')

        elif action == 'register':
            # Handle registration
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('password2')

            if not username or not email or not password or not confirm_password:
                messages.error(request, 'All fields are required.')
                return render(request, 'login.html')

            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'login.html')

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
                return render(request, 'login.html')

            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
                return render(request, 'login.html')

            try:
                # Create a new user
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                return redirect('/')
            except Exception as e:
                messages.error(request, f'Error creating account: {str(e)}')
                return render(request, 'login.html')

    return render(request, 'login.html')


def user_register(request):
        
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

            
        if not all([username, email, password, confirm_password]):
            messages.error(request, 'Please fill in all fields')
            return render(request, 'register.html')
            
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')
            
        
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html',{'form':form})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out')
    return redirect('/login')


@login_required
def user_ingridient(request):
    return render(request, 'ingridient.html')

@login_required
def user_menu(request):

    product =products.objects.all()
    price=request.GET.get('price')
    if price :
        product =products.objects.filter(price=price)

    return render(request, 'menu.html' ,{ 'products':product })