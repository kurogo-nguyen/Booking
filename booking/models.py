from django.db import models
from hotel.models import *
from user.models import User


class Reservation(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    date_from = models.DateField()
    date_to = models.DateField()
    cost = models.IntegerField(default='0')
    deposit = models.IntegerField(default='0')
    trading_code = models.IntegerField(unique=True)
    time = models.DateTimeField(auto_now_add=True)
    RESERVATION_STATUS = (
        ('confirmed', 'Confirmed'),
        ('checkedin', 'Checked in'),
        ('completed', 'Completed'),
        ('pending', 'Pending'),
        ('cancel', 'Cancel'),
    )
    status = models.CharField(choices=RESERVATION_STATUS, max_length=12, default='pending')

    class Meta:
        managed = False
        db_table = 'reservation'



class ReservationDetail(models.Model):
    room_number = models.ForeignKey(Room, models.DO_NOTHING, db_column='room_number')
    reserv = models.ForeignKey(Reservation, models.DO_NOTHING)
    ROOM_STATUS = (
        ('checked in', 'Checked in'),
        ('checked out', 'Checked out'),
        ('confirmed', 'Confirmed'),
        ('cancal', 'Cancal'),
    )
    status = models.CharField(choices=ROOM_STATUS, max_length=11)

    class Meta:
        managed = False
        db_table = 'reservation_detail'
        unique_together = ('room_number', 'reserv')


class Review(models.Model):
    reserv = models.OneToOneField(Reservation, models.DO_NOTHING, primary_key=True)
    title = models.CharField(max_length=20)
    rating = models.CharField(max_length=1)
    comment = models.CharField(max_length=500, blank=True, null=True)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'review'
