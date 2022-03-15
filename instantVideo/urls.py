from django.urls import path
from instantVideo.views import index

urlpatterns = [
    path("", index, name="index"),
]
