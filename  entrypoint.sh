#!/bin/bash

set -e

python manage.py makemigrations
python manage.py migrate

echo "from django.contrib.auth.models import User; \
if not User.objects.filter(username='admin').exists(): \
    User.objects.create_superuser('admin', 'admin@gmail.com', '12345678')" | python manage.py shell

exec "$@"