from django import forms
from .models import RegModels
class RegForm(forms.ModelForm):
    class Meta:
        model=RegModels
        fields=['FName','LName','UserName','Password','CPassword','Emailid','MobileNo']
        widgets={'Password':forms.PasswordInput(),
                 'CPassword':forms.PasswordInput()}