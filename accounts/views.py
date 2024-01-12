from typing import Any, Dict
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, UpdateView

from .forms import CustomUserChangeForm
from .models import CustomUser 
from pages.models import Products 


class UserDetailView(DetailView):
    model = CustomUser
    template_name = "account/contactuser/user_detail.html"
    context_object_name = "user_object"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Products.objects.filter(user=context["user_object"], is_moderated=True)
        context["current_user"] = self.request.user
        return context

class UserListView(ListView):
    model = CustomUser
    queryset = CustomUser.objects.filter(is_staff=False)
    template_name = "account/contactuser/user_list.html"
    context_object_name = "users"
    paginate_by = 5

class UserUpdateView(UpdateView):
    model = CustomUser
    # fields = ("last_name", "first_name", "last_name", "avatar", "taxpayer")
    form_class = CustomUserChangeForm
    template_name = "account/contactuser/user_update.html"
    success_url = reverse_lazy('homepage')