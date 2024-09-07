from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)
    

class UserRegistrationFrom(forms.ModelForm):
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