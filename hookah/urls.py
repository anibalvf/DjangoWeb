from django.urls import path, include
from hookah.views import firstview

urlpatterns = [
    path('',firstview, name = 'fi'),
]