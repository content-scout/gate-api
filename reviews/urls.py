from django.conf.urls import url, include

from . import views


urlpatterns = [
    url(r'^content/(?P<movie_id>[\d*])', views.content, name='content'),
    url(r'^add_review/(?P<movie_id>[\d*])', views.add_review, name='add'),
    url(r'^', views.search, name='search'),
]
