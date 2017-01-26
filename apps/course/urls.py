from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^drop_course/(?P<id>\d+)$', views.drop_course),
    url(r'^final_drop/(?P<id>\d+)$', views.final_drop),

]
