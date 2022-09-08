from django.contrib import admin

# Register your models here.
from .models import User, PostsModel

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}


admin.site.register(User)
admin.site.register(PostsModel,PostAdmin)