from . import  views
from django.urls import path
from register import views as v

urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts, name="contacts"),
    path("profile/", views.profile, name="profile"),
    path("classes/<int:class_id>", views.classroom, name="classroom"),
    path("classes/<int:class_id>/enroll", views.enroll, name="enroll"),
    path("classes/<int:class_id>/drop", views.drop, name="drop"),
    path("explore/", views.explore, name="explore"),
    path("search/", views.search, name="search"),
    path("classes/<int:class_id>/friends", views.friends, name="friends")
]