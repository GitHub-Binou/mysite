from django.contrib import admin
from django.apps import apps

events = apps.get_app_config('events')

for model_name, model in events.models.items():
    admin.site.register(model)
