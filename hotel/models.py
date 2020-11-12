# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=15)
    phone = models.IntegerField()
    manager_id = models.IntegerField(db_column='managerID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hotels'

    def __str__(self):
        return self.name


class Room(models.Model):
    hotel_id = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hid')  # Field name made lowercase.
    room_type = models.CharField(db_column='roomType', max_length=1)  # Field name made lowercase.
    quantity = models.IntegerField(default='0')
    img = models.CharField(db_column='rImg', max_length=50, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(default='0')

    class Meta:
        # managed = False
        db_table = 'room'
        unique_together = ('hotel_id', 'room_type')

    def __str__(self):
        name = self.hotel_id.__str__() + " -  " + self.room_type.__str__()
        return name
