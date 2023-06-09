from django import forms

class RegForm(forms.Form):
    FirstName=forms.CharField(max_length=10)
    LastName=forms.CharField(max_length=20)
    UserName=forms.CharField(max_length=20)
    Password=forms.CharField(max_length=10,widget=forms.PasswordInput)
    ConfirmPassword=forms.CharField(max_length=10,widget=forms.PasswordInput)
    Emailid=forms.EmailField()
    MobileNo=forms.CharField(max_length=13)