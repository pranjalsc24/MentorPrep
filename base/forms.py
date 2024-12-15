from dataclasses import field, fields
from importlib.abc import ExecutionLoader
from pyexpat import model
from django import forms
from django.forms import ModelForm, inlineformset_factory
from .models import  Document, Room, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
       
class CustomUserCreationForm(UserCreationForm):
    # Add a choice field for the user's role
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('mentor', 'Mentor'),
    )

    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def clean_role(self):
        role = self.cleaned_data['role']
        # Ensure the role is either 'student' or 'mentor'
        if role not in ['student', 'mentor']:
            raise forms.ValidationError("Invalid role")
        return role
      

class CompleteProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['summary', 'github', 'linkedin', 'industry', 'job_role', 'personal_details']
        
# videoupload/forms.py
from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']
        
        
        
##document form 
class DocumentForm(forms.ModelForm):
    is_public = forms.BooleanField(initial=False, required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = Document
        fields = ['file', 'description', 'is_public']