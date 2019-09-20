from django import forms
from django.contrib.auth.models import User
from .models import ContactModel, PostModel,ProfileModel
from ckeditor.widgets import CKEditorWidget


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs = {
            'class' : 'form-control',
            'placeholder' : 'Şifrə'
        }
    ))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']

        widgets = {
            'first_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Ad',
                'required data - validation - required - message' : "Please enter your name."
            }),

            'last_name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Soyad',
                'required data - validation - required - message': "Please enter your surname."
            }),

            'email' : forms.EmailInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Email',
                'required data - validation - required - message': "Please enter your email."
            }),
            'username' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder': 'Username',
                'required data - validation - required - message': "Please enter your username."
            })
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={                                                                     
            'class' : 'form-control',
            'placeholder' : 'username'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'password'
        }
    ))


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = [ 'name', 'email', 'phone', 'message']

        widgets = {
            'name' : forms.TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message',
                'rows' : "5"
            }),
        }


class SettingsForm(forms.Form):
    Ad = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder' : 'Ad'
        }
    ))

    Soyad = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder': 'Soyad'
        }
    ))
    Email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ))

    Image = forms.ImageField()


class PostForm(forms.ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = PostModel
        fields = ['title', 'subtitle', 'text', 'background_image']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),

            'subtitle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Subtitle'
            }),

        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['profile_image']

        widgets = {
            'profile_image': forms.FileInput(attrs={
                'type':"file",
                'class' : "form-control-file" ,
                'id': "exampleFormControlFile1"
            })
        }




