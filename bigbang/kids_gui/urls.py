from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),

    # ex: /home/5/
    url(r'^2/$', views.detail, name='detail'),
]
