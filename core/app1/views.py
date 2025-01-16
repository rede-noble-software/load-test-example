from django.http import JsonResponse
from django.db import transaction
from .models import Event, Ticket

@transaction.atomic
def create_event_and_ticket(request, event_name):
    event, created = Event.objects.get_or_create(name=event_name)
    # Create a new ticket for the event
    ticket = Ticket.objects.create(event=event)

    return JsonResponse({"status": "success", "message": f"Event {'created' if created else 'updated'}", "ticket_id": ticket.id})

@transaction.atomic
def book_ticket(request, ticket_id):
    if not Ticket.objects.filter(id=ticket_id).exists():
        return JsonResponse({"status": "error", "message": "Ticket does not exist"})
    
    ticket = Ticket.objects.select_for_update().get(id=ticket_id)
    if ticket.is_valid:
        return JsonResponse({"status": "error", "message": "Ticket already booked"})
    
    ticket.is_valid = True
    ticket.save()
    return JsonResponse({"status": "success", "message": "Ticket booked"})