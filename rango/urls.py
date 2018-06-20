"""rango app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path


from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/',views.about, name='about'),
    path('category/<slug:category_name_slug>/',views.show_category,name='show_category'),
    path('add_category/',views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/',views.add_page,name='add_page'),
    path('restricted/', views.restricted, name='restricted'),
    path('goto/', views.track_url, name='goto'),
    path('register_profile/', views.register_profile, name='register_profile'),
    path('profile/<slug:username>/', views.profile, name='profile'),
]
