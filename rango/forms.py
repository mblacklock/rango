from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile

#------- OVERIDE EMAIL AS USERNAME -----------
from registration.forms import RegistrationForm

class MyRegForm(RegistrationForm):
    username = forms.CharField(max_length=150, required=False, widget=forms.HiddenInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        self.cleaned_data['username'] = email
        return email
#------------------------------

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=Category.max_length,
            help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=Page.max_length,
            help_text="Please enter the title of the page.")
    url = forms.CharField(max_length=Page.max_length,
            help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
    
        # What fields do we want to include in our form?
        # This wa y we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        # or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not (url.startswith('http://') or url.startswith('https://')):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=UserProfile.max_length, required=False)
    website = forms.CharField(max_length=UserProfile.max_length, required=False)
    picture = forms.ImageField(required=False)

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = UserProfile
        fields = ('name', 'website', 'picture')
