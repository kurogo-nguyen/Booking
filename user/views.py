from tabination.views import TabView
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.views.generic import ListView, DetailView
from .models import User
# from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    return render(request, 'pages/home.html')


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'pages/register.html', {"form": form})


class SpamTab(TabView):
    _is_tab = True
    tab_id = 'spam'
    tab_group = 'main_navigation'
    tab_label = 'Spam'
    template_name = 'pages/user.html'


class ReservationsListView(ListView):
    queryset = User.objects.all()
    template_name = 'pages/user.html'
    context_object_name = 'reservations'
