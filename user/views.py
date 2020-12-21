# from tabination.views import TabView
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import ListView, DetailView
# from .models import User
from booking.models import Reservation

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.views import LoginView, LogoutView

User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'pages/home.html')

class SiteLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    form = CustomUserCreationForm()
    return render(request, 'pages/register.html', {"form": form})

class ReservationsListView(ListView):
    queryset = User.objects.all()
    template_name = 'pages/profile.html'
    context_object_name = 'reservations'

@login_required()
def CustomerProfileView(request):
    my_bookings = Reservation.objects.all().filter(user=request.user.id)
    num_bookings = len(my_bookings)
    form = ProfileEditForm(instance =  request.user)
    pass_form = PasswordChangeForm(request.user)
    if request.method == "POST":
        if 'first_name' in request.POST:
            form = ProfileEditForm(request.POST, instance= request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile was successfully updated!')
                return redirect('/profile')
        elif 'new_password1' in request.POST:
            pass_form = PasswordChangeForm(request.user, request.POST)
            if pass_form.is_valid():
                user = pass_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('/profile')      
    content = {
        'form': form,
        'pass_form': pass_form,
        'my_bookings': my_bookings,
        'num_bookings': num_bookings
    }
    return render(request, 'pages/profile.html', content)

@staff_member_required
def AdminPageView(request):
    return render(request, 'admin/admin-page.html')