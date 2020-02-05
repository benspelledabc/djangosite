#!/bin/bash

echo "setting permissions for migrations..."
sudo chown -R sdavison:datausr /data/django/IMRUnicorn-Django/imrunicorn

echo "Zeroing out migrations...."
python manage.py migrate --fake announcements zero
python manage.py migrate --fake farminvite zero
python manage.py migrate --fake loaddata zero

#python manage.py showmigrations
echo "Removing migraiton files..."
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete

# python manage.py showmigrations

echo "making new migrations..."
python manage.py makemigrations

echo "faking initial migration to get on track..."
python manage.py migrate --fake-initial

echo "Set permissions back after migrations."
sudo chown -R jenkins:datausr /data/django/IMRUnicorn-Django/imrunicorn

echo "restarting services..."
sudo service gunicorn restart
sudo service nginx restart