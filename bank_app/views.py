from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.shortcuts import render, redirect, get_object_or_404
 
from .forms import MemberCreationForm
from .models import Member, Branch
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):
        if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user=auth.authenticate(username=username,password=password)

          if user is not None:
            auth.login(request,user)
            return redirect('/')
          else:
            messages.info(request,"invalid credentials")
            return redirect('login')
        return render(request,"login.html")
    
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password==confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('login')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    return render(request, 'register.html')

def create_view(request):
    form = MemberCreationForm()
    if request.method == 'POST':
        form = MemberCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
            return redirect('add')
        

    return render(request, 'form.html', {'form': form})
 
def update_view(request, pk):
    members = get_object_or_404(Member, pk=pk)
    form = MemberCreationForm(instance=members)
    if request.method == 'POST':
        form = MemberCreationForm(request.POST, instance=members)
        if form.is_valid():
            form.save()
            return redirect('change', pk=pk)
    return render(request, 'form.html', {'form': form})
 
# AJAX
def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})

def newform(request):
    return render(request,'newform.html')
def logout(request):
   auth.logout(request)
   return redirect('/')

