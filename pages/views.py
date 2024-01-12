from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView
from .models import Ticket, Photo

class HomePageView(TemplateView):
    template_name = 'index.html'

class PortfolioPageView(ListView):
    model = Photo
    template_name = 'portfolio.html'
    context_object_name = 'photo_list'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class TicketPageView(FormView):
    model = Ticket
    template_name = 'ticket.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)