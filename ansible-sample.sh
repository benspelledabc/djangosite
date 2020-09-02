#!/bin/bash

ansible-playbook --private-key ~/.ssh/validPrivate-id_rsa -i myOceanHosts.ini playbook.yml
