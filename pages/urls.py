from django.urls import path

from .views import (
    home, about, allab, 
    portfolio, ticket
)
urlpatterns = [
    path("", home, name="homepage"),
    path('about/', about, name="about"),
    path("portfolio/", portfolio, name='portfolio'),
    path("ticket/", ticket, name='ticket'),
]