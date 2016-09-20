from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^thanks/$', views.test, name='test'),
    url(r'^login/$', views.login, name='login'),
    url(r'^html/$', views.httpResponse, name='html'), #TMP just debugging tool
]