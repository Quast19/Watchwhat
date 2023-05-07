from django.contrib import admin

# Register your models here.
from watchwhat_app.models import Watchwhat, StreamPlatform, Review

admin.site.register(Watchwhat)
admin.site.register(StreamPlatform)
admin.site.register(Review)