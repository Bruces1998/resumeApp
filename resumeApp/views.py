from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Education, Profile, Skill, Work_Experience
from django.contrib.auth.models import User
# Create your views here.

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

class SignUp(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class TestPage(TemplateView):
    template_name='test.html'
#
class ThanksPage(TemplateView):
    template_name='thanks.html'

class Homepage(TemplateView):
    template_name='index.html'



class ProfileCreate(CreateView,LoginRequiredMixin):
    template_name = 'profile.html'
    # form_class = ProfileForm
    success_url = reverse_lazy('resumeApp:education')
    model = Profile
    fields = ['firstname' , 'lastname' , 'image']

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super(ProfileCreate, self).form_valid(form)









class EducationCreate(CreateView,LoginRequiredMixin):
    template_name = 'education.html'
    # form_class = EducationForm
    success_url = reverse_lazy('resumeApp:skill')
    model = Education
    fields = ['name_of_institute', 'course', 'start_date', 'end_date']
    def form_valid(self, form):
        form.instance.possed_by = self.request.user

        return super(EducationCreate, self).form_valid(form)

class SkillCreate(CreateView,LoginRequiredMixin):
    template_name = 'skill.html'
    # form_class = SkillForm
    model = Skill
    success_url = reverse_lazy('resumeApp:work_experience')
    fields = ['name' ,'experience']

    def form_valid(self, form):
        form.instance.possed_by = self.request.user

        return super(SkillCreate, self).form_valid(form)



class Work_ExperienceCreate(CreateView, LoginRequiredMixin):
    template_name = 'work_experience.html'
    # form_class = Work_ExperienceForm
    model = Work_Experience
    success_url = reverse_lazy('resumeApp:summary')

    fields = ['name_of_org', 'designation','bio', 'start_date', 'end_date']
    def form_valid(self, form):
        form.instance.possed_by = self.request.user

        return super(Work_ExperienceCreate, self).form_valid(form)















class ProfileDetail(ListView, LoginRequiredMixin):
    model = Profile
    template_name = 'summary.html'


class Work_ExperienceDetail(DetailView, LoginRequiredMixin):
    model = Work_Experience
    template_name = 'summary.html'

class SkillDetail(DetailView, LoginRequiredMixin):
    model = Skill
    template_name = 'summary.html'

class EducationDetail(DetailView, LoginRequiredMixin):
    model = Education
    template_name = 'summary.html'
