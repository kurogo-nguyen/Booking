from django.apps import apps
from django.contrib import admin

# Register your models here.
for model in apps.get_app_config('booking').get_models():
    # if "auth" not in model.name:
    admin.site.register(model)
