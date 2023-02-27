from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm



def home(request):
	return render(request, "authenticate/home.html", {})

def about(request):
	
	return render(request, "about.html", {})

def contact(request):
	return render(request, "contact.html", {})

def videos(request):
	return render(request, "videos.html", {})

def gigs(request):
	return render(request, "gigs.html", {})

def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, ('error logging in')) 
			return redirect('login')
	else:
		return render(request, "login_user.html", {})

def logout_user(request):
	logout(request)
	messages.success(request, ('logged out'))
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			
			messages.success(request, ('Thanks for registering')) 
			return redirect('home')

	else:
		form = SignUpForm()

	context = {'form': form}
	return render(request, "authenticate/register.html", context)

def video1(request):
	return render(request, "video1.html", {})






