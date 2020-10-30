# IMRUnicornDjango

### Intended Uses
Use it to track your own handload data, groundhog dispatching, and deer harvests.

### See it in use
Docker Version : https://benspelledabc.me/
Service Version: <disabled, only using docker now>

### Background
For years I've had a website that stored my load data for reloading. I use this "known good" website setup to assist in learning a new language. I've done the site in VB.NET, C#, PHP, Java and now in Python. Each time I build the website I also try to add a new feature. This time, it's a log book of groundhog dispatching, deer harvests and a transition to using docker images to do the heavy lifting. Ben SpelledABC has decided to do the hosting for me this time in trade for learning how to do more Python also.

### Production
This portion needs to be updated. I'm keeping it for archive purposes, for now. If you use the docker-compose file you'll have the most success I think. Something I still need to work out is to create the folders to set permissions. The folders that aren't created by default are created when you try to upload pictures. Such as: folders within

### Data Backup/Restore
Really I'm just using mysqldump at this time.

### Notes
After you pull the containers via docker compose, you'll likely have to import all the migrations. I've made the 'work-it.sh' for myself but you get the idea, I hope. Make right, will make the permissions right (enough).

`./work-it.sh`
`./make_right.sh`

I'm keeping this part around just because it might prove useful again, for something else.
Don't forget to open SELinux a little to allow the proxy via gunicorn

`chcon system_u:object_r:container_file_t:s0 imrunicorn.sock`

/var/log/nginx/nginx.vhost.error.log


Jenkins takes care of my deployments now.


# raw bug
unicorn_web_1  | 2020/10/10 22:33:18 [emerg] 7#7: BIO_new_file("/opt/app/certs/selfsigned.pem") failed (SSL: error:02001002:system library:fopen:No such file or directory:fopen('/opt/app/certs/selfsigned.pem','r') error:2006D080:BIO routines:BIO_new_file:no such file)
unicorn_web_1  | nginx: [emerg] BIO_new_file("/opt/app/certs/selfsigned.pem") failed (SSL: error:02001002:system library:fopen:No such file or directory:fopen('/opt/app/certs/selfsigned.pem','r') error:2006D080:BIO routines:BIO_new_file:no such file)
imrunicorn_unicorn_web_1 exited with code 1
imrunicorn_unicorn_web_1 exited with code 1
