#!/bin/sh
openssl genrsa -out private_key_file 2048
openssl rsa -pubout -in private_key_file -out public_key_file
# RSAだと秘密鍵から公開鍵が作れる
