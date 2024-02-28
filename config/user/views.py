from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from . forms import CustomUserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import userUpdateForm,profileUpdateForm

# Create your views here.

def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,"Invalid Username or Password")
        else:
                messages.error(request,"Invalid Username or Password")
        
    else:
        form = AuthenticationForm()

    return render(request,'user/login.html',{'form':form})
    
        
def logoutUser(request):
     logout(request)
     messages.success(request,'Successfully Logout')
     return redirect('login')



def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successfull")
            return redirect('login')
        else:
            messages.error(request,"Form Invalid or empty")
    else:
        form = CustomUserCreationForm()
    return render(request,'user/signup.html',{'form':form})



# class profileView(LoginRequiredMixin,generic.View):
#     def get(self,request):
       
#         return render(request,'user/profile.html',)
#     def post(self,request):
#         ...






class profileView(LoginRequiredMixin, generic.View):
    def get(self, request):
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.userprofiledata)
        return render(request, 'user/profile.html', {'u_form': u_form, 'p_form': p_form})
    
    def post(self, request):
        u_form = userUpdateForm(request.POST, instance=request.user)
        p_form = profileUpdateForm(request.POST, request.FILES, instance=request.user.userprofiledata)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
        else:
            # Handle invalid form submission
            # You may want to render the form again with validation errors
            return render(request, 'user/profile.html', {'u_form': u_form, 'p_form': p_form})

    
    
    
    
