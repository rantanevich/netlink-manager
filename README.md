# netlink-manager

Web UI to manage static routes and network addresses with netlink.



## Requirements

* RHEL / CentOS 7
* Python 3.6+
* Running as root (only root can use netlink socket)



## Installation

Prepare a server and install the latest version:
```sh
# without HTTP(s) proxy
ansible-playbook -i srv-app-01, deploy/main.yml -e ansible_user=sshuser

# with HTTP(s) proxy
ansible-playbook -i srv-app-01, deploy/main.yml \
                 -e ansible_user=sshuser \
                 -e http_proxy='http://user:pass@host:port' \
                 -e https_proxy='http://user:pass@host:port'
```

Updating:
```sh
# without HTTP(s) proxy
ansible-playbook -i srv-app-01, deploy/main.yml -e ansible_user=sshuser

# with HTTP(s) proxy
ansible-playbook -i srv-app-01, deploy/deploy.yml \
                 -e ansible_user=sshuser \
                 -e http_proxy='http://user:pass@host:port' \
                 -e https_proxy='http://user:pass@host:port'
```


## Usage

![plot](./docs/index.jpg)

![plot](./docs/routes.jpg)

![plot](./docs/addresses.jpg)
