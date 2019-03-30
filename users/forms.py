from django import forms
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, CustomUser
User = get_user_model()

# Create your Forms here:

# Creating User Form (Model):


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Conformation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password Do not match!!')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

# Custom User login Form:


class UserLoginForm(forms.Form):
    query = forms.CharField(label='Username / Email')
    passsword = forms.CharField(label='password', widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        query = self.cleaned_data('query')
        password = self.cleaned_data('password')
        user_qs_final = User.objects.filter(
            Q(username__iexact=query) |
            Q(email__iexact=query)
        ).distinct()

        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError(
                "Invalid Credentials user does not exist."
            )
        user_obj = user_qs_final.first()

        if not user_obj.check_password(password):
            raise forms.ValidationError('Credentials are not correct.')
        self.cleaned_data['user_obj'] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)


# User Register (website):
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
