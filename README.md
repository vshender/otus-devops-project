# OTUS DevOps Project

The OTUS [DevOps course](https://otus.ru/lessons/devops-praktiki-i-instrumenty/) final project.

Run the following commands to run the project on local machine:
```
$ make -e USERNAME=vshender build test    # build and test the application images

$ cp docker/.env.example docker/.env

$ docker-compose -f docker/docker-compose.yml up -d    # run the application

```

- Open http://localhost:8000/ and check the application.
- Open http://localhost:9090/ and check Prometheus.
- Open http://localhost:3000/ and check Grafana (user/password: admin/admin).

Run the following commands to deploy GitLab:
```
$ cd gitlab/terraform

$ terraform init

$ terraform apply -auto-approve

$ cd ../ansible

$ ansible-playbook playbooks/site.yml -e "docker_hub_login=<login> docker_hub_password=<password>"
...
TASK [Show GitLab password] **********************************************************************
ok: [gitlab] => {
    "msg": "GitLab credentials for the first login: username: root, password: <gitlab_password>"
}
...
```

The deployed GitLab will contain the application repositories and configured CI/CD.
