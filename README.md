# README #

# azeri Project #

### --- Create project with create-django-app module ###

First you need to install create-django-app module with bellow credentials
```sh
$ git clone https://github.com/husubeyli/create-django-app.git
$ cd create-django-app/
$ python3 install.py
```

### --- Set up new project with create-django-app module ###
Create new django project with docker container :
```sh
$ create-django-app app_name
```

This module automaticly create `app_name` file and inside the configured `docker-compose.yml` and `Dockerfile`. 
`docker-compose.py`:
```yaml
version: '3'

services:
  nginx-proxy:
    image: jwilder/nginx-proxy
    restart: "always"
    ports:
      - "80:80"
    volumes:
      - /var/run/docker.sock:/tmp/docker.sock:ro
      - ./nginx/vhost/:/etc/nginx/vhost.d:ro
      - ./nginx/conf.d/client_max_body_size.conf:/etc/nginx/conf.d/client_max_body_size.conf:ro
      - ./static/:/construction/static
      - ./media/:/construction/media
      - ./nginx/proxy.conf/:/etc/nginx/proxy.conf

  postgres:
    container_name:  postgres-db
    image:           postgres:9.6.6
    ports:
      - 5432:5432 # Bind host port 5432 to PostgreSQL port 5432
    volumes:
      - ./pgdb:/var/lib/postgresql/data
    env_file: .env
    environment:
      - LC_ALL=C.UTF-8

  web:
    container_name: construction
    build: .
    restart: "always"
    env_file: ./.env
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    # links:
    #   - postgres
    depends_on:
      - "postgres"


```
And `Dockerfile`:
```yaml

FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV DEBUG False
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
ADD . .
# RUN python manage.py collectstatic --noinput
CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000",  "construction.wsgi" ]
```

### --- Build Docker ###
After successfuly created Django app you need to Build docker bellow command:
```sh
$ cd app_name/
$ docker-compose build -d
```

----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Django inside Container #


### --- Migrate new Postgres Database ###

First you need to install Docker Helper commands
```sh
$ curl -LO https://raw.githubusercontent.com/husubeyli/docker-helper-commands/master/install.sh && bash install.sh
$ connect-docker sh app_name
Command Created by Munis
Connecting with sh  inside app_name container with docker command
/code # source /venv/bin/activate
/code # ./manage.py migrate 
```

### --- Backup database ###

If you want to backup database:
```sh
$ backup-database-docker <postgres-db-container-name>
```

### --- Restore database from dump Sql file ###

Restore database: 
```sh 
$ restore-database-docker <dump_file> <postgres-db-container-name>
```
To create your **app**, make sure youâ€™re in the same directory as manage.py and type this command: 
```
#!

$ python manage.py startapp <appname>
```



### --- Superuser ###

Create superusers using the createsuperuser command:
```
#!

$ python manage.py createsuperuser --username=joe --email=joe@example.com
```



### --- Migrate ###

By running **makemigrations**, youâ€™re telling Django that youâ€™ve made some changes to your models (in this case, youâ€™ve made new ones) and that youâ€™d like the changes to be stored as a *migration*.


```
#!

$ python manage.py makemigrations <appname>
```

Now, run **migrate** again to create those model tables in your database:


```
#!

$ python manage.py migrate
```


### --- Running tests ###

In the terminal, we can run our test:
```
#!
$ python manage.py test <appname>
```






### --- Shell ###

To invoke the Python shell, use this command:
```
#!
$ python manage.py shell
```


### --- Install dependencies ###

Installing required dependencies on virtual environment:
```
#!
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```



----------------------------------------------------------------------------------------------------------------------------------------------------------------

### --- Credits & Helpers ###
1. Extend your RAM by adding a swap file - http://stackoverflow.com/a/18335151/968751
1. Make ffmpeg executable everywhere - http://askubuntu.com/a/613799
1. FFMpeg permission denied error - http://askubuntu.com/a/478019
1. One liner ffmpeg (or other) to get only resolution? - http://askubuntu.com/a/577431 / http://stackoverflow.com/a/29585066 (json)
1. Revert to a commit by a SHA hash in Git? - http://stackoverflow.com/a/1895095

----------------------------------------------------------------------------------------------------------------------------------------------------------------

### --- Used modules & Apps ###
1. Media server: [ngnix RMTP](https://github.com/arut/nginx-rtmp-module)
1. Video edit: [ffmpeg](https://trac.ffmpeg.org/wiki/CompilationGuide/Ubuntu)
