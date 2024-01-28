from django.contrib import admin
from .models import Blog_Category, Query, Subscription, Blog_Post

# Register your models here.
admin.site.register(Blog_Category)
admin.site.register(Query)
admin.site.register(Subscription)
admin.site.register(Blog_Post)