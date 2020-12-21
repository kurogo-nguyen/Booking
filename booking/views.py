from django.shortcuts import render
from hotel.models import *
from django.http import request, HttpResponseRedirect
from django.http import HttpResponse
from .forms import *
from user.forms import ProfileEditForm
from .models import *
from datetime import datetime, timedelta

from django.contrib import messages

# Create your views here.
def index(request):
    return None

def room_view(request):
    search = SearchRoom()
    if request.method == "POST":
        room_reserved = []
        dates = request.POST.get('dates')
        if dates != None:
            check_in = datetime.strptime(dates[0:10], '%m/%d/%Y').date()
            check_out = datetime.strptime(dates[13:], '%m/%d/%Y').date()
        else:
            check_in = datetime.today()
            check_out = datetime.today() + timedelta(days=1)
        
        reserv_using = Reservation.objects.values('id').filter(date_from__lt=check_out).filter(date_to__gt=check_in) 
        room_reserved = ReservationDetail.objects.values('room_number').filter(reserv__in=reserv_using)
        type = RoomType.objects.filter(num_person=request.POST.get('capacity'))
        room_available = Room.objects.all().exclude(pk__in=room_reserved).filter(status='available', room_type__in=type)
        room_list = RoomType.objects.all().filter(room_type__in=room_available.values('room_type'))
        print(room_reserved)
        data = {'room_list': room_list, 'dates':dates, 'capacity': request.POST.get('capacity'), 'form': search, 'search':True}

        ra_id = [item.room_number for item in room_available]
        request.session['room_show'] = ra_id

        if len(room_available) == 0:
            # pass
            messages.warning(request, "Sorry No Rooms Are Available on this time period")
        response = render(request, 'pages/search.html', data)
        print(request.POST['capacity'])
    else:
        rooms = RoomType.objects.all()
        images = Image.objects.raw('SELECT * FROM image WHERE image.id in (SELECT MAX(image.id) FROM image GROUP BY image.room_type)')

        for image in images:
            print(image)
        data = {'room_list': rooms, 'form':search, 'images':images}
        response = render(request, 'pages/search.html', data)
    return response

def payment(request):
    userForm = ProfileEditForm(instance=request.user)

    dates = request.GET.get('dates')
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
    room_name = room_type
    data = {'check_in': check_in, 'check_out': check_out, 'nights': nights, 'price': price,
            'total': total, 'room_name': room_name, 'userForm':userForm}
    print(request.user)
    if request.method == "POST":
        reservation = Reservation()

        reservation.user = request.user
        reservation.date_from = check_in
        reservation.date_to = check_out
        reservation.cost = total
        reservation.trading_code = total
        reservation.save()

        # room = 
        reservation_detail = ReservationDetail(room_number=101 ,reserv=reservation)
        messages.success(request, "Congratulations! Booking Successfull")
        return redirect('booking')

    return render(request, 'pages/payment.html', data)