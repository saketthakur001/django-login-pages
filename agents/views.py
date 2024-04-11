# import logging
from django.shortcuts import render, redirect
from django.http import HttpResponseServerError, HttpResponse
# from django.contrib.auth import views as auth_views
from .models import Member
User = Member
# Create your views here.
def about(request):
    return HttpResponse("this is the about page")

def help_(request):
    return HttpResponse("this is the response page")

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'base.html', param)
    else:
        return redirect('login')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        # print(uname, pwd)
        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('Username already exists.')
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
        check_user = User.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            # return HttpResponse('user name found, you have logged in')
            return render(request, 'home')
        else:
            return HttpResponse('user don\'t exist')
            
    return render(request, 'login.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')
