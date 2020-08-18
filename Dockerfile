# Dockerfile

FROM python:3.7-buster

# install nginx
RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir -p /opt/app/imrunicorn
RUN mkdir -p /opt/app/imrunicorn/data
RUN touch /opt/app/imrunicorn/data/empty

COPY start-server.sh /opt/app/
COPY ./imrunicorn/requirements.txt /opt/app/
# COPY .pip_cache /opt/app/pip_cache/
COPY imrunicorn /opt/app/imrunicorn/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
