from django.contrib import admin

from .models import Tour, Reserv
# Register your models here.

admin.site.site_header = "Адмін панель Турів"
admin.site.register([Tour, Reserv])