import markdown
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from datetime import datetime


class Event(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=4000, null=True, blank=True)
    create_user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='/events/%Y/%m/%d', blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ("-create_date",)

    def get_content_as_markdown(self):
        return markdown.markdown(self.content, safe_mode='escape')

    @staticmethod
    def get_is_active():
        event = Event.objects.filter(active=True)
        return event

    def __str__(self):
        return self.title
