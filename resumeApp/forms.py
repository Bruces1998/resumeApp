from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Education, Profile, Skill, Work_Experience


class UserForm(UserCreationForm):
    class Meta():
        model = get_user_model()
        fields = ('username','email','password1','password2')


class EducationForm(forms.ModelForm):

    class Meta():
        model = Education
        fields = '__all__'

class ProfileForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = '__all__'






class SkillForm(forms.ModelForm):

    class Meta():
        model = Skill
        fields = '__all__'

    

class Work_ExperienceForm(forms.ModelForm):

    class Meta():
        model = Work_Experience
        fields = '__all__'
