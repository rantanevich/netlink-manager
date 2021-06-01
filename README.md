# netlink-manager

Web UI to manage static routes and network addresses with netlink.



## Requirements

* RHEL / CentOS 7
* Python 3.6+
* Running as root (only root can use netlink socket)



## Installation

Prepare a server and install the latest application's version:
```sh
ansible-playbook -i srv-app-01, deploy/main.yml
```

Update the application:
```sh
ansible-playbook -i srv-app-01, deploy/deploy.yml
```


## Usage

Information about static routes and network addresses:
![plot](./docs/index.jpg)

Adding and deleting static routes:
![plot](./docs/routes.jpg)

Adding and deleting network addresses:
![plot](./docs/addresses.jpg)
