# IMRUnicornDjango

### Intended Uses

Stuff.


### Production

This portion needs to be updated. I'm keeping it for archive purposes, for now. If you use the docker-compose file you'll have the most success I think. Something I still need to work out is to create the folders to set permissions. The folders that aren't created by default are created when you try to upload pictures. Such as: folders within

    /opt/app/imrunicorn/media

    ```sh
    $ docker-compose -f docker-compose.yml up -d --build
    $ docker-compose -f docker-compose.yml exec unicorn_web python imrunicorn/manage.py makemigrations --no-input
    $ docker-compose -f docker-compose.yml exec unicorn_web python imrunicorn/manage.py migrate --no-input
    $ docker-compose -f docker-compose.yml exec unicorn_web python imrunicorn/manage.py collectstatic --no-input --clear
    $ docker-compose -f docker-compose.yml exec -it unicorn_web python imrunicorn/manage.py createsuperuser
    $ empty stuff:   docker-compose -f docker-compose.yml down -v

    ```
    Exec into the web container to create a superuser.



### Data Backup/Restore

Really I'm just using mysqldump for now but this might work too.

backup: ./manage.py dumpdata --natural-foreign --exclude contenttypes --exclude auth.permission --exclude admin.logentry --exclude sessions.session --indent 4 > ~/iWantItAll3.json

restore: ./manage.py loaddata ~/iWantItAll3.json




### Notes
Don't forget to open SELinux a little to allow the proxy via gunicorn

`chcon system_u:object_r:container_file_t:s0 imrunicorn.sock`
