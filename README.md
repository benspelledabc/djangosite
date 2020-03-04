# IMRUnicornDjango
repo created by pycharm


dont forget to open SELinux a little to allow the proxy via gunicorn
`chcon system_u:object_r:container_file_t:s0 imrunicorn.sock`


backup: ./manage.py dumpdata --natural-foreign --exclude contenttypes --exclude auth.permission --exclude admin.logentry --exclude sessions.session --indent 4 > ~/iWantItAll3.json

restore: ./manage.py loaddata ~/iWantItAll3.json


### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    $ docker-compose -f docker-compose.prod.yml exec web python manage.py makemigrations --no-input
    $ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --no-input
    $ docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
    ```
    Exec into the web container to create a superuser.
    ```sh
    ~/web $ ./manage.py createsuperuser
    Username (leave blank to use 'app'): bobsyouruncle
    Email address: 
    ...etc etc...
    ```

    Test it out at [http://localhost](http://localhost). No mounted folders. To apply changes, the image must be re-built.
