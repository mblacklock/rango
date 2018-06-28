import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'free_bets_project.settings')

import django
django.setup()

from datetime import datetime

from rango.models import Category, Page#, Quiz, QuizScore, User, UserProfile

def populate():
    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/",
              "views": 1},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/",
              "views": 2},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/",
              "views": 3} ]

    django_pages = [
             {"title":"Official Django Tutorial",
              "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
              "views": 15},
             {"title":"Django Rocks",
              "url":"http://www.djangorocks.com/",
              "views": 23},
             {"title":"How to Tango with Django",
              "url":"http://www.tangowithdjango.com/",
              "views": 33} ]

    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/",
              "views": 45},
        {"title":"Flask",
         "url":"http://flask.pocoo.org",
              "views": 54} ]

    pascal_pages = [ ]
    perl_pages = [ ]
    php_pages = [ ]
    prolog_pages = [ ]
    postscript_pages = [ ]
    programming_pages = [ ]

##    python_scores = [{"user":"dave","score":5},{"user":"dave","score":7}]
##    django_scores = [{"user":"dave","score":5}]
##    other_scores = [{"user":"dave","score":5}]
##    pascal_scores = [{"user":"dave","score":5}]
##    perl_scores = [{"user":"dave","score":5}]
##    php_scores = [{"user":"dave","score":5}]
##    prolog_scores = [ ]
##    postscript_scores = [{"user":"dave","score":5}]
##    programming_scores = [ ]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16},
            "Pascal": {"pages": pascal_pages, "views": 128, "likes": 64},
            "Perl": {"pages": perl_pages, "views": 128, "likes": 64},
            "PHP": {"pages": php_pages, "views": 128, "likes": 64},
            "Prolog": {"pages": prolog_pages, "views": 128, "likes": 64},
            "PostScript": {"pages": postscript_pages, "views": 128, "likes": 64},
            "Programming": {"pages": programming_pages, "views": 128, "likes": 64}
            }

##    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64,
##                       "quiz": {"out_of": 10, "attempts": 1}, "scores": python_scores},
##            "Django": {"pages": django_pages, "views": 64, "likes": 32,
##                       "quiz": {"out_of": 11, "attempts": 2}, "scores": django_scores},
##            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16,
##                                 "quiz": {"out_of": 12, "attempts": 3}, "scores": other_scores},
##            "Pascal": {"pages": pascal_pages, "views": 256, "likes": 128,
##                       "quiz": {"out_of": 13, "attempts": 4}, "scores": pascal_scores},
##            "Perl": {"pages": perl_pages, "views": 512, "likes": 256,
##                     "quiz": {"out_of": 14, "attempts": 5}, "scores": perl_scores},
##            "PHP": {"pages": php_pages, "views": 1024, "likes": 512,
##                    "quiz": {"out_of": 15, "attempts": 6}, "scores": php_scores},
##            "Prolog": {"pages": prolog_pages, "views": 2048, "likes": 1024,
##                       "quiz": {"out_of": 16, "attempts": 7}, "scores": python_scores},
##            "PostScript": {"pages": postscript_pages, "views": 4096, "likes": 2048,
##                           "quiz": {"out_of": 17, "attempts": 8}, "scores": postscript_scores},
##            "Programming": {"pages": programming_pages, "views": 8192, "likes": 4096,
##                            "quiz": {"out_of": 18, "attempts": 9}, "scores": programming_scores}
##            ,}
##
##    users = {"dave": {"website":"http://dave.com"},
##             "andy": {"website":"http://andy.com"},
##             "steve": {"website":"http://steve.com"},
##             "john": {"website":"http://john.com"},
##             "fred": {"website":"http://fred.com"}
##             }

    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data["views"],cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])

##        quiz = add_quiz(c,cat_data["quiz"]["out_of"],cat_data["quiz"]["attempts"])
##        print("- Quiz - " + cat)
##
##        for q in cat_data["scores"]:
##            user = User.objects.get(username=q['user'])
##            add_quiz_score(user,quiz,q['score'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

##    for u, u_data in users.items():
##        add_user(username=u)
##        print("- " + str(u))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat,title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

##def add_user(username,password="demo12345678",email="demo@demo.com"):
##    u = User.objects.get_or_create(username=username)[0]
##    u.set_password(password)
##    u.email = email
##    u.save()
##    return u
##
##def add_quiz(cat,out_of,attempts):
##    q = Quiz.objects.get_or_create(category=cat)[0]
##    q.out_of = out_of
##    #q.attempts = attempts
##    q.is_active = True
##    q.save()
##    return q
##
##def add_quiz_score(user,quiz,score=0):
##    s = QuizScore.objects.get_or_create(quiz=quiz,user=user,score=score)[0]
##    s.save()
##    return s

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
