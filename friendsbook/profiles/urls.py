from django.urls import path
from . import views

appname="profiles"

urlpatterns = [
    path('myprofile/',views.my_profile_view,name="myprofile"),
]
