from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Repeat password')

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'middle_name']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(
                attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password2'):
            raise forms.ValidationError('Passwords are not equal')
        return cd.get('password2')


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            qs = CustomUser.objects.filter(email=email)
            if not qs.exists():
                raise forms.ValidationError('User does not exists')
        return super(LoginForm, self).clean()