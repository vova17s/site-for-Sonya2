from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('portfolio/', views.PortfolioPageView.as_view(), name='portfolio'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('ticket/', views.TicketPageView.as_view(), name='ticket'),
]
