from django.urls import path
from django.conf.urls import url
from . import views
from .views import StandardCalculator
urlpatterns = [
    path('',views.index, name='index'),
    url('standard/', StandardCalculator.as_view(), name="standard-calculator"),
]