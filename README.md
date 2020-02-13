# IMRUnicornDjango
repo created by pycharm


dont forget to open SELinux a little to allow the proxy via gunicorn
`chcon system_u:object_r:container_file_t:s0 imrunicorn.sock`


backup: ./manage.py dumpdata --natural-foreign --exclude contenttypes --exclude auth.permission --exclude admin.logentry --exclude sessions.session --indent 4 > ~/iWantItAll3.json

restore: ./manage.py loaddata ~/iWantItAll3.json
