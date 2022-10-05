from django.conf.urls import include, url
from users.views import register

urlpatterns = [
    url(r"^register/", register, name="register"),
]