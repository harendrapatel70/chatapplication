from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ChatHistory
from .rules import chatbot_response
# Create your views here.

def home(request):
    return render(request, 'home.html')

def register_view(request) :
    if request.method == "POST" :
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        User.objects.create_user(username=username,email=email,password=password)
        messages.success(request, "account created successfully")
        return redirect('login')
    
    return render(request,'register.html')


def login_view(request) :
    if request.method == "POST" :
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('chat')
        else :
            messages.error(request, "Invalid credentials")
    return render(request,'login.html')

def logout_view(request) :
    logout(request)
    return redirect('login')

@login_required
def change_password(request) :
    if request.method == "POST" :
        new_password=request.POST['password']
        request.user.set_password(new_password)
        request.user.save()
        return redirect('login')
    return render(request,'change_password.html')

@login_required
def chat_view(request):
    if request.method == "POST":
        user_msg = request.POST.get("message")
        bot_msg = chatbot_response(user_msg)

        ChatHistory.objects.create(
            user=request.user,
            question=user_msg,
            answer=bot_msg
        )

        return redirect('chat')

    chats = ChatHistory.objects.filter(user=request.user)
    return render(request, "chat.html", {"chats": chats})