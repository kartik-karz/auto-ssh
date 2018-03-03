#!/usr/bin/expect

#set timeout 20



set name [lindex $argv 0]
set email [lindex $argv 1]
set comment [lindex $argv 2]
set pass [lindex $argv 3]

spawn /usr/bin/gpg --gen-key

expect "Your selection?" { send "1\r" }
expect "What keysize do you want?" { send "4096\r" }
expect "Key is valid for?" {send "0\r"}
expect "Is this correct?" {send "y\r"}
expect "Real name" {send "$name\r"}
expect "Email address" {send "$email\r"}
expect "Comment" {send "$comment\r"}
expect "Change" {send "O\r"}
expect "Enter passphrase" {send "$pass\r"}
expect "Repeat passphrase" {send "$pass\r"}
interact
