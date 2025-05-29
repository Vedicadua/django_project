# django_project
django_project


#for run celery worker:
celery -A email_project worker --loglevel=info

#Celery beat scheduler
celery -A email_project beat --loglevel=info

#Django server
python manage.py runserver

#for run without celery
curl -X POST http://127.0.0.1:8000/send-email/ \
-H "Content-Type: application/json" \
-d '{
    "subject": "Test Email",
    "message": "Hello from Django!",
    "from_email": "sender@example.com",
    "recipient_list": ["recipient@example.com"]
}'




