from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Command)
admin.site.register(Match)
admin.site.register(Circulation)
admin.site.register(User)
admin.site.register(BetInfo)
