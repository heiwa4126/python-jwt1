#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103, C0111
"""
minimum example
https://ymstmsys.hatenablog.jp/entry/2022/02/05/144106
"""
import jwt
import cryptography

# pipではなく Ubuntu の python3-cryptography パッケージを使った(気がついたら入ってた)。
# pyjwt も python3-jwt を使用。


def main():
    with open("private_key_file", "r") as f:
        private_key = f.read()

    payload_data = {"id": "001", "name": "kobayashi", "age": 25, "gender": "boy"}

    token = jwt.encode(payload=payload_data, key=private_key, algorithm="RS256")
    # https://jwt.io/ でsecretにpublic_key_fileの中身を入れればverifyされる

    print(token)


if __name__ == "__main__":
    main()
