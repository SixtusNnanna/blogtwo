from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DetailView, UpdateView
from.forms import SignUpForm, EditForm,password1Form,CreateProfileForm
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profile


def DetailedUserProfileView(request, pk):
    model = Profile
    template_name = 'registration/user_profile_detail_page.html'

    def get_context_data(self, *args)


class UpdateUserProfileView(UpdateView):
    model = Profile
    template_name = 'registration/user_profile_update_page.html'
    form_class = CreateProfileForm
    

class CreateUserProfileView(CreateView):
    model = Profile
    template_name = 'registration/user_profile_creation_page.html'
    form_class = CreateProfileForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PassWordChangingView(PasswordChangeView):
    form_class = password1Form
    success_url = reverse_lazy('blog:home')
    template_name='registration/passwordchange.html'

class RegisterUserView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(UpdateView):
    form_class = EditForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('blog:home')

    def get_object(self):
        return self.request.user


