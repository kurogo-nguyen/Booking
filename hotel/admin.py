from django.apps import apps
from django.contrib import admin

from .models import *

# Register your models here.

class ImageInLine(admin.TabularInline):
    model = Image 
    fields =('image_tag','image')
    readonly_fields = ['image_tag']
    extra = 3

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number','room_type','status')

class RoomTypeAdmin(admin.ModelAdmin):
    inlines = [ImageInLine]
    list_display = ('room_type', 'price', 'num_person')
    fieldsets = (('Info', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('room_type', 'price', 'num_person'),
        }),)


admin.site.register(Room, RoomAdmin)
admin.site.register(RoomType, RoomTypeAdmin)