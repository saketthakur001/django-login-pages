from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponse
# from django.contrib.auth import views as auth_views
from .models import Member

# Create your views here.
def about(request):
    return HttpResponse("this is the about page")

def help_(request):
    return HttpResponse("this is the response page")

def home(request):
    if 'user' in requet.session:
        current_user = request.session['user']
        param = {'current_user': current_user}
        return render(request, 'base.html', parm)
    else:
        return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        print(uname, pwd)
        if Member.objects.filter(username=uname).count()>0:
            return HttpResponse('Username already exists')
        else:
            user = Member(username=uname, password=pwd)
            user.save()
            return redirect('login')
    else:
        return render(request, 'signup.html')

    # return render(request, "home.html")

def login(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user = Member.objects.filter(username=uname, password=pwd)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        else:
            return HttpResponse('Please enter valid Username or Password')
    