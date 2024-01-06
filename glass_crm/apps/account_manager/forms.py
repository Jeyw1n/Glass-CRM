from django import forms
from django.contrib.auth import get_user_model


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput( attrs={'class': 'form-input'}))
    
    class Meta():
        model = get_user_model()
        fields = ['username', 'password']
        
        
class RegisterUserForm(forms.Form):
    username = forms.CharField(label="Логин",)    
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput())
    
    class Meta():
        model = get_user_model()
        fields = ['username', 'password', 'password2']
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != ['password2']:
            raise forms.ValidationError("Пароли не совпадают!")
        return cd['password']