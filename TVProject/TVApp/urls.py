from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/<int:show_id>', views.detail),
    path('shows/<int:show_id>/edit', views.edit),
    path('shows/add', views.add_show),
    path('shows/<int:show_id>/update', views.update_show),
    path('shows/<int:show_id>/delete', views.delete),
]