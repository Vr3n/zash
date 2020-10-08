from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import CustomUser

# Create your views here.

# Function for User Registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}!')
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form, 'title':'Register'})

# Function to View Profile
@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,
                            instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                               request.FILES,
                               instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account Updated!!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)

# Function for changing Password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # if we don't pass this The user session will be terminated and have to login again.
            messages.success(request, 'Your passsword was successfully changed!!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error!!')
    else:
        c_form = PasswordChangeForm(request.user)
    
    context = {
        'c_form':c_form  
    }

    return render(request, 'users/change_password.html', context)

# # REST serializer.

# class UserViewSet(viewsets.ModelViewSet):
#     """ API endpoint that allows users to be Viewed and Edited """
#     queryset = CustomUser.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
