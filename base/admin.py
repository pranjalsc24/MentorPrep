from django.contrib import admin
from .models import Room, Topic, Message
# from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)