from django.urls import path
from . import views

urlpatterns=[
    path("",views.home),
    path("destination",views.destination),
    path("deals",views.deals),
    path("contact",views.contact)
]