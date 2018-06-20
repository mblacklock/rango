# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    max_length = 128
    name = models.CharField(max_length = max_length, unique=True)
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Page(models.Model):
    max_length = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length = max_length)
    url = models.CharField(max_length = max_length)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    slug = models.SlugField(unique=False)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(UserProfile, self).save(*args, **kwargs)
    
    max_length = 128
    name = models.CharField(max_length = max_length, blank=True)
    website = models.CharField(max_length = max_length, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
    
