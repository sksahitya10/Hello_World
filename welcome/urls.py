from django.urls import re_path
from . import views
urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    #127.0.0.1/welcome/
    re_path(r'^(?P<question_id>[0-9]+)/$',views.detail,name="welcome.detail"),
    #127.0.0.1/welcome/2
    re_path(r'^(?P<question_id>[0-9]+)/results$',views.results,name="results"),
    #127.0.0.1/welcome/2/results
    re_path(r'^(?P<question_id>[0-9]+)/vote$',views.vote,name="welcome.vote"),
    #127.0.0.1/welcome/2/vote
]