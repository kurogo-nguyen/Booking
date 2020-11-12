from django.db import models
from hotel.models import *
from user.models import User


class Reservation(models.Model):
    hid = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hid')
    uid = models.ForeignKey(User, models.DO_NOTHING, db_column='uid')  # Field name made lowercase.
    date_from = models.DateField(db_column='date-from')  # Field renamed to remove unsuitable characters.
    date_to = models.DateField(db_column='date-to')  # Field renamed to remove unsuitable characters.
    cost = models.IntegerField(default='0')
    deposit = models.IntegerField(default='0')
    trading_code = models.IntegerField(db_column='tradingCode', unique=True)  # Field name made lowercase.
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'reservation'


# Create your models here.
class ReservationDetail(models.Model):
    room_id = models.ForeignKey(Room, models.DO_NOTHING, db_column='roomID')
    reservation_id = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='reservID')
    quantity = models.IntegerField(default='0')

    class Meta:
        managed = False
        db_table = 'reservation_detail'
        unique_together = ('room_id', 'reservation_id')


class Review(models.Model):
    reservation_id = models.OneToOneField(Reservation, models.DO_NOTHING, primary_key=True, db_column='reservID')
    title = models.CharField(max_length=20)
    rating = models.CharField(max_length=1)
    comment = models.TextField(max_length=500, blank=True, null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'review'
