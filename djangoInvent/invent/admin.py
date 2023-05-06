from django.contrib import admin
from .models import Kab, Inventar

admin.site.register(Kab)
admin.site.register(Inventar)

admin.site.site_header="Администрирование инвентаря"

# Register your models here.
