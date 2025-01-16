from django.contrib import admin
from django.urls import path
from core.app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("create-event-and-ticket/<str:event_name>/", views.create_event_and_ticket),
    path("book-ticket/<int:ticket_id>/", views.book_ticket, name="book_ticket"),
]
