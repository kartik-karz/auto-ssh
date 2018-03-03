# Auto SSH 

auto-ssh is a simple gui to easily create a ssh passkey and Gpg keys via RSA for adding to 
various online repositories like Github, Gitfoss easily.

## Beware
auto-ssh is still in alpha and may contain bugs, to terminate the program click the x icon for the gui and/or press ctr^c for terminal.
### Installation

Auto SSH requires [PyQt5](https://pypi.python.org/pypi/PyQt5) to display GUI elements.

To Install it on your machine you need to install
- Pyqt5
- Git ( if you haven't already)
- expect (sudo apt install expect)

You can install the dependencies by 
```sh
$ cd auto-ssh
$ pip3 install -r requirements.txt
$ python3 package/app.py
```
### Usage
- Type your name, email-id and password, and press ssh for generating ssh key and gpg for gpg keys.
- Generating gpg keys will take some time due to entropy requirements for 4096R so please be patient.
- For ssh go to your terminal and retype the password to allow the ssh-agent to add the 
  RSA key.
- For Gpg after the entropy requirements are met you will be provided the keys in the layout.
- Copy the key provided and add it to Github,Gitfoss or elsewhere.
- Enjoy

Note: Pressing submit without input will result in error.

Note: If you already have an RSA key it will ask for overwriting permission.

License
----

MIT
