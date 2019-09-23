from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'status','created_on', 'content')
    list_filter = ("status",'slug')
    search_fields = ['slug','content']
    #prepopulated_fields = {'slug': ('S',)}

admin.site.register(Post, PostAdmin)