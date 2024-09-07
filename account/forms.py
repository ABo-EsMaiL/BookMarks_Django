from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)
    

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    repeatPassword = forms.CharField(label='repeat password',widget=forms.PasswordInput)
    
    class Meta:
        model =User
        fields = ['username','email','first_name']
        
    
    def clean_repeatPassword(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeatPassword']:
            raise forms.ValidationError('passwords do not match')
        return cd['repeatPassword']
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already exists.')
        return data
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Email already exists.')
        return data
    
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_birth', 'photo','phone_number']