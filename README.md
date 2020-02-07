# IMRUnicornDjango
repo created by pycharm


dont forget to open SELinux a little to allow the proxy via gunicorn
`chcon system_u:object_r:container_file_t:s0 imrunicorn.sock`
