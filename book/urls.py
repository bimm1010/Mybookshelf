from django.urls import path
from . import views
app_name = 'book'
urlpatterns = [
    path('', views.showoff, name="show"),
    
]
