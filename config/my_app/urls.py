from django.urls import path, include
from .views import birthday_view, birthday_archive, delete_wishevent, edit_wishevent
urlpatterns = [
    
    path("index", birthday_view, name = "index"),
    path("wish-list/", birthday_archive, name = "wish-list"),
    path("wish-list/delete/<int:pk>", delete_wishevent, name = "wish-delete"),
    path("wish-list/edit/", edit_wishevent, name = "wish-edit"),
]
