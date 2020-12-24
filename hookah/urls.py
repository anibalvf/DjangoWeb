from django.urls import path, include
from hookah.views import firstview

urlpatters = [
    path('',firstview, name = 'fi'),
]