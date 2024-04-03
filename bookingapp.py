from azure.servicebus import ServiceBusClient, ServiceBusMessage
import json

conn_str = ""
queue_name = "booking-requests"

def submit_booking_request(booking_details):
    client = ServiceBusClient.from_connection_string(conn_str)
    with client.get_queue_sender(queue_name) as sender:
        message_body = json.dumps(booking_details)
        message = ServiceBusMessage(message_body)
        sender.send_messages(message)
        print("Booking request submitted successfully.")
        
booking_details = {
    "user_id": "123",
    "booking_date": "2024-04-03",
    "booking_time": "10:00 AM",
    "booking_details": "Room reservation for conference."
}

submit_booking_request(booking_details)
