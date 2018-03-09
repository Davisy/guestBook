from django.contrib import admin
from .models import Comment 
# Register your models here.

#allow you to modify the comment on the admin dashboard 
admin.site.register(Comment) 