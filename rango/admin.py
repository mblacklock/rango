# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from rango.models import Category, Page, UserProfile

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'url']

class UserProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('user',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

