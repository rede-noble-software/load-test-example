from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
class Event(models.Model):
    name = models.CharField(max_length=100, unique=True)
    booked_tickets = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="tickets")
    is_valid = models.BooleanField(default=False)

@receiver(post_save, sender=Ticket)
def update_event_bookings(sender, instance, **kwargs):
    # Simulate contention by querying and updating the related Event
    print(f"Updating event {instance.event.name} bookings")
    event = Event.objects.select_for_update().get(name=instance.event)
    event.booked_tickets = event.tickets.filter(is_valid=True).count()
    event.save()