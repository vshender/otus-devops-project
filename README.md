# OTUS DevOps Project

The OTUS [DevOps course](https://otus.ru/lessons/devops-praktiki-i-instrumenty/) final project.

Run the following commands to run the project on local machine:
```
$ make -e USERNAME=vshender build test    # build and test the application images

$ cp docker/.env.example docker/.env

$ docker-compose -f docker/docker-compose.yml up -d    # run the application

```

Open http://localhost:8000/ and check the application.
