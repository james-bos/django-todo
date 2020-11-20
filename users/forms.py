from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Blog

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"