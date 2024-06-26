# import logging
from django.shortcuts import render, redirect
from django.http import HttpResponseServerError, HttpResponse
from django.contrib import messages
# from django.contrib.auth import views as auth_views
from .models import Member
from django.contrib.auth import authenticate

User = Member
# Create your views here.
def about(request):
    return HttpResponse("this is the about page")

def help_(request):
    return HttpResponse("this is the response page")

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        print("sql query: ", current_user)
        return render(request, 'home.html', {'current_user': current_user})
    else:
        messages.error(request, 'You will have to login first to access Home page!!')
        return redirect('login')
    # return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        print(uname, pwd)
        if Member.objects.filter(username=uname).count()>0:
            messages.error(request, 'User already regestered!')
            return redirect('login')
        else:
            user = User(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        print(f'got the uname and pwd {uname}, {pwd}')
        check_user = User.objects.filter(username=uname, password=pwd)
        print(User.objects.all())
        # user = authenticate(request, username=uname, password=pwd)
        print(check_user)
        if check_user:
            request.session['user'] = uname
            # return HttpResponse('user name found, you have logged in')
            return redirect('home')
        else:
            messages.error(request, 'username or password incorrect!')
            # return HttpResponse('user does not exist')
    if 'user' in request.session:
        current_user = request.session['user']
        # return render(request, 'home.html', {'current_user': current_user})
        return redirect('home')
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')
