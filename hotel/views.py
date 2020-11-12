from django.shortcuts import render, redirect
from user.models import User
from .forms import createHotel
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hotel


# Create your views here.
@login_required(login_url='/login')
def index(request):
    user = request.user
    form = createHotel(initial={'manager_id': user.id})
    form.fields['manager_id'].widget = forms.HiddenInput()
    if request.method == 'POST':
        form = createHotel(request.post)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'pages/createHotel.html', {"user": user, "form": form})

# def userView(request):
#     user = User.uname
#     recommend = {"hotels": Hotels.objects.get()}
#     return render(request, 'pages/home.html', user, recommend)
