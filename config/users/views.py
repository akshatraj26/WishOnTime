from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def home(request):
    return render(request, 'authenticate/home.html', {})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful")
            print("Login  Successful")
            return redirect('index')
        else:
            messages.error(request, "Username or password is incorrect")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})
    
    
def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            subject = "Welcome Mail"
            message = "Thank you for registering with WishOnTime! We are thrilled to have you on board"
            
            html_message = render_to_string("authenticate/welcome.html", {
                'name': name,
                'username': username,
                'password': password,
                "message": message
            })
            
            send_mail(subject,
                      message,
                      settings.DEFAULT_FROM_EMAIL,
                      [email],
                      fail_silently=False,
                      html_message=html_message
                      )
            
            print("Mail sent successfully")
            messages.success(request, "Registration Successful.")
            
            return redirect('login')
        else:
            messages.error(request, "Registraion Unsuccessful! Invalid details.")
            
    else:
        form = RegisterForm()
        
    return render(request, "authenticate/register.html", {'form': form})
            

