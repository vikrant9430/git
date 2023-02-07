from django.urls import path, include
from . import views


urlpatterns = [
    path("new/", views.employee),
    path("this-is-employee-profile-page/", views.profile, name="profile")

]
