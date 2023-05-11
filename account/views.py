from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages, auth
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.models import User
from contacts.models import Contacts

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')

        else:
            messages.error(request, 'You are not registerd')
            return redirect('login')

    else:
        return render(request, 'account/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logout')
        return redirect('index')


def register(request):
    # Get form values
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, email=email, first_name=first_name, last_name=last_name, password=password)

                    # auth.login(request, user)
                    user.save()
                    messages.success(
                        request, 'You registerd successfuly and can now login')
                    return redirect('login')

        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

    else:
        return render(request, 'account/Register.html')


def dashboard(request):
    
    contacts = Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id )

    
    context = {
        'contacts' : contacts
    }
    return render(request, 'account/dashboard.html', context )
