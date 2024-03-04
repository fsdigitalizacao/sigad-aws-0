from django.urls import path
from . import views
app_name = 'sigad'

urlpatterns = [
    path('', views.home_view, name='sigad_home'),
]