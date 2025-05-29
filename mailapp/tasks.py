from celery import shared_task
from django.core.mail import send_mail
import logging
import random

logger = logging.getLogger(__name__)

@shared_task
def send_scheduled_email():
    # Generate a random subject and message
    subjects = [
        "Scheduled Email",
        "Hello from Django!",
        "This is a Random Subject",
        "Daily Update",
        "Celery Task Notification"
    ]
    messages = [
        "This email was sent automatically.",
        "Your random message is here!",
        "Have a great day!",
        "Celery sends you a greeting.",
        "Here is your scheduled notification."
    ]
    # Pick random subject and message
    subject = random.choice(subjects)
    message = random.choice(messages)

    # You can randomize recipient too, e.g., pick from a list
    recipient_options = [
        "recipient1@example.com",
        "recipient2@example.com",
        "recipient3@example.com"
    ]
    recipient_list = [random.choice(recipient_options)]

    from_email = "sender@example.com"

    try:
        send_mail(subject, message, from_email, recipient_list)
        logger.info(f"Scheduled email sent successfully to {recipient_list} with subject '{subject}'")
    except Exception as e:
        logger.error(f"Failed to send scheduled email: {str(e)}")
