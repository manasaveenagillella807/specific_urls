from django.urls import path

from rcb.views import *

urlpatterns=[
    path('kohli/',kohli,name='kohli'),
]