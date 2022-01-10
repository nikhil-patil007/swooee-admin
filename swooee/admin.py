from django.contrib import admin
from .models import *
from .models import *
from mptt.admin import MPTTModelAdmin

# Show On Admin Panel
class productadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'discription', 'category', 'Image', 'created_at', 'updated_at', 'status')
    list_display_links = ('id', 'name', 'slug')
    list_filter = ('category'),
    # list_editable = ('updated_at',)
    search_fields = ('name','category')
    ordering = ('category',)
    
class Static_pageadmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug','created_at', 'updated_at', 'status')
    list_display_links = ('id', 'title', 'slug')
    

# Register your models here.
admin.site.register(Categories, MPTTModelAdmin)
admin.site.register(Product,productadmin)
admin.site.register(User)
admin.site.register(Admin_user)
admin.site.register(Static_page,Static_pageadmin)
admin.site.register(Banner)