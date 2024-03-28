from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login,logout
from django.contrib import messages
from .models import TodoList
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    if request.method =='POST':
        tasks=request.POST.get('user_task')
        new_task_add=TodoList(user=request.user,task=tasks)
        if TodoList.objects.filter(task=new_task_add).exists():
            # messages.error(request, 'Task already exists')
            return redirect('home-page')
        new_task_add.save()
    
    all_tasks=TodoList.objects.filter(user=request.user)
    username=request.user.username
    context={
        'tasks_list': all_tasks,
        'usernames': username
        }
    return render(request, 'todo/home.html', context)
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        
        user_details=authenticate(username=username,password=password)
        if user_details is not None:
            login(request,user_details)
            return redirect('home-page')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login')
    return render(request, 'todo/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists, Try another')
            return redirect('registerpath')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists , Please Login')
            return redirect('loginpath')
        
        
        if len(password) < 5 or len(password) >15:
            messages.error(request, 'Password must be at least 5 characters or Max 15 Characters')
            return redirect('registerpath')
       
        if password!=password2:
            messages.error(request,'Confirm Password Mismatch')
            return redirect('registerpath')
    
        
        new_user=User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, 'User created successfully')
        return redirect('loginpath')
    
    return render(request,'todo/register.html')

def Userlogout(request):
    logout(request)
    return redirect('loginpath')
@login_required 
def delete_tasks(request,name):
    get_task=TodoList.objects.get(user=request.user, task=name)
    get_task.delete()
    return redirect('home-page')
@login_required
def update_tasks(request,name):
    get_task=TodoList.objects.get(user=request.user, task=name)
    get_task.status=True
    get_task.save()
    return redirect('home-page')
    