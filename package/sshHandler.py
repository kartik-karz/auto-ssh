#!/usr/bin/python3

import subprocess as sb
import os

SSH_KEY_GEN = "ssh-keygen -t rsa -b 4096 -C "

# USER_EMAIL = '"test2@example.com"'


def create_key(email_id,password):
    global SSH_KEY_GEN
    rsa_file_path = os.path.expanduser('~/.ssh/id_rsa')
    SSH_KEY_GEN = SSH_KEY_GEN +  email_id
    command = SSH_KEY_GEN.split(" ")
    command.append(" -N ")
    command.append(password)
    command.append(" -f ")
    command.append(rsa_file_path)
    # print(command)
    command_str = " ".join(command)
    os.system(command_str)
    # sb.call(command)
def add_to_agent():
    os.system('"eval "$(ssh-agent -s)"')
    os.system("ssh-add ~/.ssh/id_rsa")

# create_key("test2@test.com","password")
