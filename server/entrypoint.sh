#!/bin/bash
echo "=======LOAD MODULE========"
echo $DJANGO_SETTINGS_MODULE
echo "=========================="
python manage.py makemigrations
python manage.py migrate
# echo "=======COLLECTING STATIC========"
# python manage.py collectstatic --no-input
# echo "=========================="
supervisord -c /etc/supervisor/conf.d/supervisord.conf -n
