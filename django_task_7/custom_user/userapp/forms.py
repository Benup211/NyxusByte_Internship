from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
            return None
        else:
            return confirm_password
    def check_email_exists(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return None
        else:
            return email
    def send_verification_email(self, user):
        subject = 'Account Verification'
        verification_link = render_to_string('userapp/verify_user.html', {'user': user})
        from_email = settings.EMAIL_HOST_USER
        to_email = user.email
        send_mail(subject, '', from_email, [to_email], html_message=verification_link)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.is_active = False
        if commit:
            user.save()
            self.send_verification_email(user)