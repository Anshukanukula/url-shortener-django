from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_short_url, name="create_short_url"),
    path("list/", views.list_all_urls, name="list_all_urls"),  # ⬅ Add this BEFORE the dynamic path
    path("<str:short_code>/", views.redirect_url, name="redirect_url"),
]
