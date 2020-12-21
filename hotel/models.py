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
    manager_id = models.IntegerField(db_column='managerID')

    class Meta:
        db_table = 'hotels'

    def __str__(self):
        return self.name

class Image(models.Model):
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type')
    image = models.ImageField(upload_to='room_images')

    class Meta:
        managed = False
        db_table = 'image'

    def image_tag(self):
        from django.utils.html import mark_safe
        return mark_safe('<img src="{}" width="auto" height="100px" />'.format(self.image.url))
    image_tag.short_description = 'View'

    def __str__(self):
        return self.room_type.__str__()

class Room(models.Model):
    room_number = models.SmallIntegerField(primary_key=True)
    room_type = models.ForeignKey('RoomType', models.DO_NOTHING, db_column='room_type')
    status = models.CharField(
        max_length=32,
        choices=(
            ('available', 'Available'),
            ('using', 'Using'),
            ('not clean', 'Need Clean'),
            ('boken', 'Broken'),
        ),
        default = 'available',
    )

    class Meta:
        db_table = 'room'

class RoomType(models.Model):
    room_type = models.CharField(primary_key=True, max_length=30)
    price = models.IntegerField(default='0')
    description = models.TextField()
    NUM_PEOPLE = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('family', 'Family'),
    )
    num_person = models.CharField(choices=NUM_PEOPLE, max_length=10)
    area = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'room_type'
    
    def __str__(self):
        return self.room_type
