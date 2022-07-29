from django import views
from django.urls import path
from .views import *

urlpatterns = [
    path('<int:match>/<str:mismatch>/<str:gap>/<str:seqA>/<str:seqB>/<str:algorithm>', helloWorld)
]