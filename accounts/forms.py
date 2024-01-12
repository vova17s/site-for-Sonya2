from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm, forms.Form):
    username = forms.CharField(
        max_length=30, label=None, required=True,
        widget=forms.TextInput(attrs={      
            'class': 'form_line',
            'placeholder': 'Никнейм'
        }))

    first_name = forms.CharField(
        max_length=30, label=None, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Имя'
        }))

    middle_name = forms.CharField(
        max_length=30, label=None, required=False,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Отчество',
            'for': 'id_avatar'
        }))

    last_name = forms.CharField(
        max_length=30, label=None, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Фамилия'
        }))

    email = forms.EmailField(
        label=None, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Почта'
        }))

    telegram_url = forms.URLField(
        required=True, label=None,
        widget=forms.URLInput(
            attrs={
                'class': 'form_line',
                'placeholder': 'Telegram'
            }))

    avatar = forms.ImageField(
        required=True, label='Загрузить фото',
        widget=forms.FileInput(attrs={
            'for': 'profile',
            'class': 'form_image_input',
        }))

    taxpayer = forms.IntegerField(
        min_value=1, max_value=99999999999999, required=True, label=None,
        widget=forms.TextInput(
            attrs={
                'class': 'form_line',
                'placeholder': 'ИНН'
            }))

    password1 = forms.CharField(label=None, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form_line'}))
    password2 = forms.CharField(label=None, widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'class': 'form_line'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name','middle_name', 'last_name', 'telegram_url', 'email', 'taxpayer', 'password1', 'password2', 'avatar',)


class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(
        max_length=30, label=None, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Имя'
        }))

    middle_name = forms.CharField(
        max_length=30, label=None, required=False,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Отчество',
            'for': 'id_avatar'
        }))

    last_name = forms.CharField(
        max_length=30, label=None, required=True,
        widget=forms.TextInput(attrs={
            'class': 'form_line',
            'placeholder': 'Фамилия'
        }))

    avatar = forms.ImageField(
        required=True, label='Загрузить фото',
        widget=forms.FileInput(attrs={
            'for': 'profile',
            'class': 'main_button form_button',
        }))

    telegram_url = forms.URLField(
        required=True, label=None,
        widget=forms.URLInput(
            attrs={
                'class': 'form_line',
                'placeholder': 'Telegram'
            }))

    taxpayer = forms.IntegerField(
        min_value=1, max_value=99999999999999, required=True, label=None,
        widget=forms.TextInput(
            attrs={
                'class': 'form_line',
                'placeholder': 'ИНН'
            }))

    password = None

    class Meta:
        model = CustomUser
        fields = ('last_name', 'first_name','middle_name', 'telegram_url', 'taxpayer', 'avatar')

