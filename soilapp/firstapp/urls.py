from django.urls import path
from . import views

# SET THE NAMESPACE!
app_name = 'firstapp'

urlpatterns=[
    path('',views.index,name='index'),
]
