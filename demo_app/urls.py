from django.conf.urls import url
from demo_app import views
from demo_app.views import *

urlpatterns = [
    url(r'^$', views.homepage, name='home'),

]
