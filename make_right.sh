#!/bin/bash

echo "Making directories needed for image storage."
docker exec -it $1_unicorn_web_1 mkdir -p /opt/app/imrunicorn/media/uploads/announcements/what_is_new
docker exec -it $1_unicorn_web_1 mkdir -p /opt/app/imrunicorn/media/uploads/deer_shots
docker exec -it $1_unicorn_web_1 mkdir -p /opt/app/imrunicorn/media/uploads/groundhog_kill_shots


echo "Setting Permissions"
docker exec -it $1_unicorn_web_1 chown -R www-data:www-data /opt/app/imrunicorn

# echo "Making migrations and stuff..."
# docker exec benspelledabc_unicorn_web_1 ./imrunicorn/manage.py makemigrations
# docker exec benspelledabc_unicorn_web_1 ./imrunicorn/manage.py migrate
# docker exec benspelledabc_unicorn_web_1 ./imrunicorn/manage.py collectstatic --no-input
# docker exec -it benspelledabc_unicorn_web_1 ./imrunicorn/manage.py createsuperuser

echo "Happy dockering!"
