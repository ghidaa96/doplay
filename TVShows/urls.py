from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	 
    path('shows',views.shows),
    path('shows/new',views.shownew),
    path('shows/create',views.newShow),
    path('shows/<num>',views.show),
    path('shows/<num>/edit',views.edit),
    path('shows/<num>/update',views.update),
    path('shows/<num>/destroy',views.destroy)
]