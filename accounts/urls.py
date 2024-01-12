from django.urls import path, include

from .views import UserListView, UserDetailView, UserUpdateView


urlpatterns = [
    path("", include("allauth.urls")),
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("list/", UserListView.as_view(), name="user_list"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
]