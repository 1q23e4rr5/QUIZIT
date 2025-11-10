from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, QuizSettings
from django.core.validators import RegexValidator

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9@.+_-]+$',
                message='نام کاربری فقط می‌تواند شامل حروف انگلیسی، اعداد و علامات @/./+/-/_ باشد.',
                code='invalid_username'
            ),
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'نام کاربری (فقط حروف انگلیسی و اعداد)'
        }),
        help_text='حداکثر 150 کاراکتر. فقط حروف انگلیسی، اعداد و @/./+/-/_ مجاز هستند.'
    )
    
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'ایمیل (اختیاری)'
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'رمز عبور'
        }),
        help_text='رمز عبور باید حداقل 8 کاراکتر باشد و نباید فقط از اعداد تشکیل شده باشد.'
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'تکرار رمز عبور'
        }),
        help_text='برای تأیید، رمز عبور را دوباره وارد کنید.'
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('این نام کاربری قبلاً ثبت شده است.')
        return username

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'نام کاربری'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'رمز عبور'
        })
    )

class QuizSettingsForm(forms.ModelForm):
    class Meta:
        model = QuizSettings
        fields = ['total_questions', 'points_per_correct', 'points_per_wrong', 'is_active']
        widgets = {
            'total_questions': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 50}),
            'points_per_correct': forms.NumberInput(attrs={'class': 'form-control'}),
            'points_per_wrong': forms.NumberInput(attrs={'class': 'form-control'}),
        }