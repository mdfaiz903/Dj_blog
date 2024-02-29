from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash,get_user_model
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from . forms import CustomUserCreationForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import userUpdateForm,profileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

User_model = get_user_model()

# Create your views here.
@login_required
def Pass_change(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form = PasswordChangeForm(data=request.POST,user=request.user)
                    # PasswordChangeForm(data=request.POST,user = request.user)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.success(request,"Successfully Password Changed")
                return redirect('login')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'user/password_change.html',{'form':form})
   
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
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activate Your Account"
            message = render_to_string('user/account.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            send_mail = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject,message,to=[send_mail])
            email.send()
            messages.info(request,'Successfully created account, Please check your Mail box')
            return  redirect('login')
        else:
            messages.error(request,"Form Invalid or empty")
    else:
        form = CustomUserCreationForm()
    return render(request,'user/signup.html',{'form':form})

def activate(request,uidb64,token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User_model._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User_model.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        messages.success(request,'Your account is activate now,you cant now login')
        return redirect('login')
    else:
        messages.warning(request,'Activation link is Invalid')
        return redirect('signup')


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

    
    
    
    
