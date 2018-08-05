from first_app import views
from django.conf.urls import url

app_name='first_app'
urlpatterns=[
    url(r'^$', views.index, name = 'index'),
]
