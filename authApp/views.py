from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required#special functions that modify behaviors of other functions' code without having to invoke orig funcs.
from django.contrib.auth.mixins import LoginRequiredMixin #verifies current user is authenticated, for class-based views (cbv)
from django.views import View #for class-based views (cbv)
from django.contrib.auth.models import User #import the user class (model)
from .forms import RegisterForm #import reg form from forms.py
        
def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('home')
    else:
        form=RegisterForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            # Handle 'next' parameter if present, otherwise redirect to home
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else: 
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    # Ensure the template is rendered for GET requests
    return render(request, 'accounts/login.html')

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('logout_page')

#home view, using the decorator
@login_required
def home_view(request):
    return render(request,'auth1_app/home.html')

#protected view
class ProtectedView(LoginRequiredMixin,View):
    login_url='/accounts/login/'
    #'next' = to redirect url (usual one)
    redirect_field_name='next'
    def get(self,request):
        return render(request,'registration/protected.html')