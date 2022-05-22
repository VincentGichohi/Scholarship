from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from validation.models import MyUser

User = get_user_model()

class RegisterForm(forms.ModelForm):
    """
    The default
    """

    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email']

    def clean(self):
        """
        Verify email is available
        """
        email = self.cleaned_data.get('email')
        qs = MyUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is already taken")
        return email

    def clean(self):
        """
        Verify both emails match
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password is not None and password != password2:
            self.add_error('password2', 'Your passwords must match')
        return cleaned_data


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required fields plus a 
    repeated password
    """
    password = forms.CharField(widget=forms.PasswordInput)
    password_2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ['email']


    def clean(self):
        """
        Verify both passwords match.
        """
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_2 = cleaned_data.get('password2')
        if password is not None and password != password_2:
            self.add_error('password_2', 'Your passwords must match')
        return cleaned_data

    def save(self, commit=True):
        #Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        


