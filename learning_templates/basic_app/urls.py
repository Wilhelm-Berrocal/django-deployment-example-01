from django.urls import path, re_path, include
from . import views

# Template tagging
app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
