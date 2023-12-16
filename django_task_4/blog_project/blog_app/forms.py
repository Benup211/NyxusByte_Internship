from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label='username',max_length=50)
    password=forms.CharField(label='password',max_length=50)
class Createblog(forms.Form):
    title=forms.CharField(label="title")
    content=forms.CharField(label="content")
    pub_date=forms.DateTimeField(label="pub_date")
    tag=forms.CharField(label="tag")