# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template.defaultfilters import slugify

# Import Models & Forms
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

# Create your views here.

def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pages': pages_list}
	
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html', context={})

def show_category(request, category_name_slug):

    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)
        
        context_dict['pages'] = pages
        context_dict['category'] = category
        
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        try:
            # check if category already exists
            Category.objects.get(slug=slugify(request.POST["name"]))
            return render(request, 'rango/add_category.html', {'form':form, 'slug_exists':True})
        except Category.DoesNotExist:
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return index(request)
            else:
                print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):

    try:
        # check if page already exists
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)

