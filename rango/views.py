# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Import Models & Forms
from rango.models import Category, Page, UserProfile
from rango.forms import CategoryForm, PageForm, UserProfileForm

# Create your views here.

def index(request):

    request.session.set_test_cookie()
    visitor_cookie_handler(request)

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list,
                    'pages': pages_list,
                    'visits': request.session['visits'],
                    'last_visit': datetime.strptime(request.session['last_visit'][:-7],
                                        '%Y-%m-%d %H:%M:%S')}
	
    return render(request, 'rango/index.html', context=context_dict)


def about(request):

    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED")
        request.session.delete_test_cookie()
        
    # prints out whether the method is a GET or a POST
    print(request.method)
    # prints out the user name, if no one is logged in it prints `AnonymousUser`
    print(request.user)
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

@login_required
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

@login_required
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

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html', {})

@login_required
def change_password(request):
    return render(request, 'registration/password_change_form.html', {})

def track_url(request):
    url = '/rango/'
    try:
        page_id = request.GET['page_id']
        try:
            page = Page.objects.get(id=page_id)
            page.views = page.views + 1
            page.save()
            url = page.url
        except:
            pass
    except:
        pass

    return redirect(url)

@login_required
def register_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('rango:index')
        else:
            print(form.errors)

    context_dict = {'form':form}

    return render(request, 'registration/registration_profile.html', context_dict)

@login_required
def profile(request, userid):
    try:
        user = User.objects.get(id=userid)
        userprofile = UserProfile.objects.get(user=user)
    except User.DoesNotExist:
        return redirect('rango:index')
    
    form = UserProfileForm(
        {'name': userprofile.name, 'website': userprofile.website, 'picture': userprofile.picture})
    if request.method == 'POST' and request.user.username == user.username:
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('rango:profile', user.id)
        else:
            print(form.errors)
    return render(request, 'registration/profile.html',
            {'userprofile': userprofile, 'selecteduser': user, 'form': form})

@login_required
def user_list(request):
    user_list = UserProfile.objects.all()
    print(user_list)
    return render(request, 'rango/user_list.html', {'user_list': user_list})


###########  HELPER FUNCTIONS  ###############

def visitor_cookie_handler(request):
    # Get the number of visits to the site.
    # We use the COOKIES.get() function to obtain the visits cookie.
    # If the cookie exists, the value returned is casted to an integer.
    # If the cookie doesn't exist, then the default value of 1 is used.
    visits = int(get_server_side_cookie(request,'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).seconds > 2:
        visits += 1
        #update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] =  last_visit_cookie
    # update/set the visits cookie
    request.session['visits'] =  visits

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


          
