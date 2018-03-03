import subprocess as sb
import os


def create_key(name,email_id,comment,password):
    sb.call(["expect","./session_scripts/gpgGen.sh",name,email_id,comment,password])

def load_gpg_key():
    getIdCommand = 'gpg --list-secret-keys --keyid-format LONG | cut -d " " -f 4|sed -n 3p | cut -c 7-'
    gpgPubId = sb.check_output(getIdCommand,shell=True)
    gpgPubId = str(gpgPubId,"utf-8")

    exportGpgKeyCommand =  "gpg --armor --export "+ gpgPubId
    pubGpgKey = sb.check_output(exportGpgKeyCommand,shell=True)
    pubGpgKey = str(pubGpgKey,"utf-8")

    return pubGpgKey

# create_key("test","test@mail.com","nothing","password")
