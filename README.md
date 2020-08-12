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
    $ docker-compose -f docker-compose.yml up -d --build
    $ docker-compose -f docker-compose.yml exec unicorn_web python manage.py imrunicorn/makemigrations --no-input
    $ docker-compose -f docker-compose.yml exec unicorn_web python manage.py imrunicorn/migrate --no-input
    $ docker-compose -f docker-compose.yml exec unicorn_web python manage.py imrunicorn/collectstatic --no-input --clear
    $ empty stuff:   docker-compose -f docker-compose.yml down -v

    ```
    Exec into the web container to create a superuser.
    ```sh
    ~/web $ ./manage.py createsuperuser
    Username (leave blank to use 'app'): bobsyouruncle
    Email address: 
    ...etc etc...
    ```

    Test it out at [http://localhost](http://localhost). No mounted folders. To apply changes, the image must be re-built.
