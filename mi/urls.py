from django.urls import path

from mi.views import *

urlpatterns=[
    path('panday/',panday,name='panday')
]