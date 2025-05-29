#!/bin/bash

# Start Gunicorn server for Django (foreground)
gunicorn email_project.wsgi:application --bind 0.0.0.0:3000  > /mnt/logs/application.log 2>&1 &

# Wait a few seconds to make Gunicorn start listening
sleep 5

# Start Redis server in the background
redis-server > /mnt/logs/redis.log 2>&1 

sleep 5

# Start Celery worker in the background
celery -A email_project worker > /mnt/logs/celery_worker.log 2>&1 &

# Start Celery Beat in the background
celery -A email_project beat > /mnt/logs/celery_beat.log 2>&1 &

# Wait for Gunicorn (PID 1) to exit
wait -n

# Exit with status of the first process to exit
exit $?
