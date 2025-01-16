from locust import HttpUser, task, between
import random

class TicketBookingUser(HttpUser):
    wait_time = between(0.5,1)  # Wait time between tasks

    @task(1)
    def book_ticket(self):
        """
        Simulate booking a ticket by sending a GET request to the book_ticket endpoint.
        """
        ticket_id = random.randint(1, 1000)
        self.client.get(f"/book-ticket/{ticket_id}/")


    @task(1)
    def create_event_and_ticket(self):
        """
        Simulate creating an event and ticket by sending a GET request.
        """
        event_name = "Coldplay"
        self.client.get(f"/create-event-and-ticket/{event_name}/")
    
    @task(1)
    def create_event_and_ticket_lg(self):
        """
        Simulate creating an event and ticket by sending a GET request.
        """
        event_name = "LadyGaga"
        self.client.get(f"/create-event-and-ticket/{event_name}/")
