import json
import logging
import threading
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

# Configure logging
logger = logging.getLogger(__name__)

# Function to send emails
def send_email_in_background(subject, message, from_email, recipient_list):
    try:
        send_mail(subject, message, from_email, recipient_list)
        logger.info(f"Email sent successfully to {recipient_list}")
    except Exception as e:
        logger.error(f"Failed to send email: {str(e)}")

# Django view to trigger email sending
@csrf_exempt  # For testing purposes, disables CSRF protection (use cautiously)
def send_email_view(request):
    if request.method != 'POST':
        logger.warning("Non-POST request made")
        return HttpResponseBadRequest("Only POST requests are allowed.")

    try:
        data = json.loads(request.body)
        subject = data["subject"]
        message = data["message"]
        from_email = data["from_email"]
        recipient_list = data["recipient_list"]

        # Validate recipient_list is a list
        if not isinstance(recipient_list, list):
            raise ValueError("recipient_list must be a list of emails.")

        logger.info(f"Received request to send email from {from_email} to {recipient_list}")

        # Run email sending in a background thread
        threading.Thread(
            target=send_email_in_background,
            args=(subject, message, from_email, recipient_list),
        ).start()

        return JsonResponse({"status": "Email is being sent in the background"})

    except (KeyError, json.JSONDecodeError, ValueError) as e:
        logger.error(f"Invalid input data: {str(e)}")
        return HttpResponseBadRequest(f"Invalid input data: {str(e)}")
