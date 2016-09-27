# SeeThisProperty.com
![Python Version](https://img.shields.io/badge/Python-2.7-green.svg)
![Django Version](https://img.shields.io/badge/Django-1.9-green.svg)

#### Running on Nginx and Gunicorn
/etc/nginx/sites-available/seethisproperty
```
upstream gunicorn_seethisproperty {
	# For a TCP configuration:
	server 127.0.0.1:9000 fail_timeout=0;
}

server {
	listen 80;
	client_max_body_size 4G;
	server_name seethisproperty.com *.seethisproperty.com;

	keepalive_timeout 5;

	location /static/ {
	   alias /var/www/html/seethisproperty/stp-django/realestate/realestate/static/;
	   expires 30d;
	}

	location / {
	    # checks for static file, if not found proxy to app
	    try_files $uri @proxy_to_app;
	}

	location @proxy_to_app {
	    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
	    proxy_set_header Host $http_host;
	    proxy_redirect off;

	    proxy_pass   http://gunicorn_seethisproperty;
	}
}

```

/var/html/www/seethisproperty/seethisproperty-env/bin/gunicorn_start.sh
```
#!/bin/bash

NAME="seethisproperty"                                  # Name of the application
DJANGODIR=/var/www/html/seethisproperty/stp-django/realestate             # Django project directory
NUM_WORKERS=3                                     # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=realestate.settings             # which settings file should Django use
DJANGO_WSGI_MODULE=realestate.wsgi                     # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /var/www/html/seethisproperty/seethisproperty-env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec gunicorn ${DJANGO_WSGI_MODULE} \
  --bind 127.0.0.1:9000 \
  --name $NAME \
  --workers $NUM_WORKERS \
  --log-level=debug \
  --log-file=-

```
