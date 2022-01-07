from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


# Register your models here.
admin.site.register(Categories, MPTTModelAdmin)
admin.site.register(product)
admin.site.register(user)
admin.site.register(admin_user)
admin.site.register(static_page)
admin.site.register(banner)