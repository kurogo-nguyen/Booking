from django.shortcuts import render, redirect
from hotel.models import *
from django.http import request, HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from user.forms import ProfileEditForm

from django.contrib.auth.decorators import login_required
from .models import *
from datetime import datetime, timedelta
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    return None

def room_view(request):
    search = SearchRoom()
    images = Image.objects.raw('SELECT * FROM image WHERE image.id in (SELECT MAX(image.id) FROM image GROUP BY image.room_type_id)')
    if request.method == "POST":
        room_reserved = []
        dates = request.POST.get('dates')
        if dates != None:
            check_in = datetime.strptime(dates[0:10], '%m/%d/%Y').date()
            check_out = datetime.strptime(dates[13:], '%m/%d/%Y').date()
        else:
            check_in = datetime.today()
            check_out = datetime.today() + timedelta(days=1)

        reserv_using = Reservation.objects.values('room_number').filter(Q(date_from__lt=check_out, date_from__gt=check_in) | Q(date_to__gt=check_in,date_to__lt=check_out)).exclude(status='cancel')
        # room_reserved = ReservationDetail.objects.values('room_number').filter(reserv__in=reserv_using)
        type = RoomType.objects.filter(num_person=request.POST.get('capacity'))
        a = Room.objects.values('room_number').exclude(pk__in=reserv_using)
        room_available = Room.objects.all().filter(room_type__in=type, room_number__in=a)

        room_list = RoomType.objects.all().filter(pk__in=room_available.values('room_type_id'))

        paginator = Paginator(room_list, 5)
        pageNumber = request.GET.get('page')
        try:
            rooms = paginator.page(pageNumber)
        except PageNotAnInteger:
            rooms = paginator.page(1)
        except EmptyPage:
            rooms = paginator.page(paginator.num_pages)


        data = {'room_list': rooms, 'dates':dates, 'capacity': request.POST.get('capacity'), 'form': search, 'search':True, 'images':images}


        if len(room_available) == 0:
            # pass
            messages.warning(request, "Sorry No Rooms Are Available on this time period")
        response = render(request, 'pages/search.html', data)
        print(request.POST['capacity'])
    else:
        room_list = RoomType.objects.all()
        paginator = Paginator(room_list, 5)
        pageNumber = request.GET.get('page')
        try:
            rooms = paginator.page(pageNumber)
        except PageNotAnInteger:
            rooms = paginator.page(1)
        except EmptyPage:
            rooms = paginator.page(paginator.num_pages)
        images = Image.objects.raw('SELECT * FROM image WHERE image.id in (SELECT MAX(image.id) FROM image GROUP BY image.room_type_id)')
        data = {'room_list': rooms, 'form':search, 'images':images}
        response = render(request, 'pages/search.html', data)
    return response
@login_required()
def payment(request):
    userForm = ProfileEditForm(instance=request.user)

    dates = request.GET.get('date')
    if dates != None:
        check_in = datetime.strptime(dates[0:10], '%m/%d/%Y').date()
        check_out = datetime.strptime(dates[13:], '%m/%d/%Y').date()
    else:
        check_in = datetime.today()
        check_out = datetime.today() + timedelta(days=1)
    nights = (check_out -check_in).days
    room_type= request.GET.get('type')
    price = RoomType.objects.get(pk=room_type).price
    total = nights * price
    # rooms = [RoomDetail.objects.get(id=room_id) for room_id in request.session['room_show']]
    # room = RoomDetail.objects.filter(id__in=request.session['room_show'], type_id=room_type_id)[0]
    room = RoomType.objects.get(pk=room_type)
    data = {'check_in': check_in, 'check_out': check_out, 'nights': nights, 'price': price,
            'total': total, 'room': room, 'userForm':userForm}
    print(request.user)
    if request.method == "POST":

        reserv_using = Reservation.objects.values('room_number').filter(Q(date_from__lt=check_out, date_from__gt=check_in) | Q(date_to__gt=check_in,date_to__lt=check_out)).exclude(status='cancel')
        # room_reserved = ReservationDetail.objects.values('room_number').filter(reserv__in=reserv_using)
        type = RoomType.objects.filter(num_person=request.POST.get('capacity'))
        a = Room.objects.values('room_number').exclude(Q(pk__in=reserv_using) | Q(status='broken'))
        room_available = Room.objects.all().filter(room_type=room_type, room_number__in=a)[0]

        reservation = Reservation()

        reservation.user = request.user
        reservation.date_from = check_in
        reservation.date_to = check_out
        reservation.cost = total
        reservation.room_number = room_available
        # reservation.trading_code = total
        reservation.save()

        messages.success(request, "Congratulations! Booking Successfull")
        return redirect('booking')

    return render(request, 'pages/payment.html', data)