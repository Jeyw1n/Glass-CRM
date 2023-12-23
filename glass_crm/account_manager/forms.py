from django import forms

class LoginUserForm(forms.Form):
    
    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(
            attrs={'class': 'formInput'}
            )
        )
    
    password = forms.CharField(
        label="Пароль",
        widget=forms.TextInput(
            attrs={'class': 'formInput'}
            )
        )