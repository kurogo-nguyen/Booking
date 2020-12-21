from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from blog.models import Post
from hotel.models import *
from .forms import *
from user.forms import *
from hotel.forms import *
from booking.models import *
from .filters import *

from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.forms import modelformset_factory
# from django.template import RequestContext

# Create your views here.
@staff_member_required
def blog_management_view(request):
    if request.method == "GET":
        try:
            cid = request.GET.get('cid')
            blog = Post.objects.get(id=cid)
            blog.delete()
            messages.success(request, "Delete blog successfully!")
        except:
            pass
    blogs = Post.objects.all().order_by('-id')
    paginator = Paginator(blogs, 10)
    pageNumber = request.GET.get('page')
    try:
        posts = paginator.page(pageNumber)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    data = {'blogs': posts, 'nav': 'blog'}
    return render(request, 'blog/blog.html', data)

@staff_member_required
def EditPost(request, id):
    post = Post.objects.get(pk=id)
    if request.method == 'POST':
        postForm1 = PostForm(request.post, instance=post)
        if postForm1.is_valid():
            postForm1.save()

    postForm = PostForm(instance=post)
    data = {'form': postForm, 'nav': 'blog'}
    return render(request, 'blog/edit_blog.html', data)

@staff_member_required
def NewPost(request):
    print(request.user.id)
    if request.method == 'POST':
        try:
            post = PostForm(request.POST, request.FILES)
            if post.is_valid():
                post.save()
                messages.success(request, "Add new blog successfully!")
                content ={
                    'post_form': post
                }
            return render(request, 'blog/add_blog.html', content)
        except:
            pass
            # messages.error(request, obj.errors)
    else:
        post = PostForm(instance=request.user)
    content ={
        'post_form': post
    }
    return render(request, 'blog/add_blog.html', content)

@staff_member_required
def AddRoom(request):
    if request.method == 'POST':
        form = RoomForm(request.post)
        if form.is_valid():
            form.save()
            messages.success(request, "Add new room successfully!")
            return redirect('admin-room')
        else:
            messages.error(request, "Add new room fail!")
    else:
        form = RoomForm()
    return render(request, 'admin/room/add_room.html', {'form': form})

@staff_member_required
def room_view(request):
    r_id = request.GET.get('room_id')
    room_status = request.GET.get('status')
    rooms = Room.objects.all().order_by('room_number')
    myFilter = RoomFilter(request.GET, queryset=rooms)
    if r_id:
        myFilter = RoomFilter({}, queryset=rooms)
        try:
            room = Room.objects.get(room_number=r_id)
            if room_status == 'available':
                room.status = 'available'
                room.save()
            elif room_status == 'checked-out':
                room.status = 'not clean'
                room.save()
                try:
                    reservation = ReservationDetail.objects.filter(room_number=r_id, status='checked in')
                    reservation.status = 'checked out'
                    reservation.save()
                except:
                    pass
                
            elif room_status == 'checked-in':
                 room.status = 'using'
                 room.save()
            else:
                room.status = room_status
                room.save()
        except:
            pass
    rooms = myFilter.qs
    total_rooms = len(Room.objects.all())
    rooms_available = len(Room.objects.filter(status='available'))
    rooms_unavailable = len(Room.objects.filter(status='broken'))
    rooms_checked_in = len(Room.objects.filter(status='using'))

    data = {'checkedIn': rooms_checked_in, 'total_rooms': total_rooms, 'unavailable': rooms_unavailable,
            'available': rooms_available, 'rooms': rooms, 'myFilter': myFilter}
    return render(request, 'admin/room/room_detail.html', data)

@staff_member_required
def ViewAccount(request):
    # if request.method == "GET":
    #     try:
    #         cid = request.GET.get('cid')
    #         blog = User.objects.get(id=cid)
    #         blog.delete()
    #         messages.success(request, "Delete blog successfully!")
    #     except:
    #         pass
    users_list = User.objects.all().order_by('id').exclude(is_superuser='True')
    paginator = Paginator(users_list, 10)
    pageNumber = request.GET.get('page')
    try:
        users_list = paginator.page(pageNumber)
    except PageNotAnInteger:
        users_list = paginator.page(1)
    except EmptyPage:
        users_list = paginator.page(paginator.num_pages)
    data = {'accounts': users_list, 'nav': 'blog'}
    return render(request, 'admin/account/account.html', data)

def ChangeAccStatus(request, id, action):
    acc = User.objects.get(pk=id)
    if action == 'active':
        acc.is_active = True
    else:
        acc.is_active = False
    acc.save()
    return redirect('admin-account')

def RegisterAcc(request):
    if request.method == 'POST':
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    form = StaffCreationForm()
    return render(request, 'pages/register.html', {"form": form})

@staff_member_required
def room_category_view(request):
    if request.method == "GET":
        try:
            type = request.GET.get('room_number')
            category = RoomType.objects.get(pk=type)
            category.delete()
            messages.success(request, "Delete category successfully!")
        except:
            pass
    rooms = RoomType.objects.all().order_by('room_type')
    images = Image.objects.all()
    data = {'rooms': rooms, 'images': images}

    return render(request, 'admin/room/room_category.html', data)

@staff_member_required
def reservation_management_view(request):
    if request.method == "GET":
        reservation_id = request.GET.get('id')
        status = request.GET.get('status')
        try:
            reservation = Reservation.objects.get(pk=reservation_id)
            # room = Room.objects.get(id=reservation.room_id)
            if status == 'confirmed':
                # nights = (reservation.check_out - reservation.check_in).days
                # total = nights * reservation.room.type.price
                reservation.status = status
            if status == 'checkedin':
                if reservation.check_in <= date.today():
                    # room.status = 'checkedin'
                    reservation.status = status
                else:
                    messages.warning(request, "Check In isn't ready!")
            else:
                if status == 'completed':
                    # room.status = 'unavailable'
                    reservation.status = status
            reservation.status = status
            # room.save()
            # if status == 'delete':
            #     reservation.delete()
            # else:
            reservation.save()
        except:
            pass
    reservations = Reservation.objects.all()
    data = {'reservations': reservations}
    return render(request, 'admin/room/reservation_management.html', data)


def edit_category_view(request, type):
    room = RoomType.objects.get(pk=type)
    room = RoomTypeForm(instance=room)
    imgs = Image.objects.filter(room_type=type)
    images=[]
    for img in imgs:
        images.append(ImageForm(instance=img))

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            messages.success(request, "Update category successfully!")
            return redirect('room_category')

    data = {'room': room, 'images':images}
    return render(request, 'admin/room/edit_category.html', data)


@staff_member_required
def New_Room_Type(request):
    ImageFormSet = modelformset_factory(Image,
                                        form=ImageForm, extra=3)

    if request.method == 'POST':
        roomTypeForm = RoomTypeForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=Image.objects.none())


        if roomTypeForm.is_valid() and formset.is_valid():
            post_form = roomTypeForm.save(commit=False)
            # post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                image = form.get('image')
                if image != None:
                    photo = Image(room_type=post_form, image=image)
                    photo.save()
            messages.success(request, "Posted!")
            return redirect('room_category')
        else:
            print(roomTypeForm.errors, formset.errors)
    else:
        roomTypeForm = RoomTypeForm()
        formset = ImageFormSet(queryset=Image.objects.none())
    return render(request, 'admin/room/CreateRoomType.html', {'room': roomTypeForm, 'images': formset})

