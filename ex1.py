#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable-msg=C0103, C0111
"""
minimum example
https://laboratory.kazuuu.net/using-pyjwt-in-python-to-create-a-json-web-token/
"""
import jwt


def main():
    payload_data = {"id": "001", "name": "kobayashi", "age": 25, "gender": "boy"}

    token = jwt.encode(payload=payload_data, key="my_secret")
    # デフォルトはalg:HS256(事前共有鍵)なので、
    # https://jwt.io/ でsecretにmy_secretを入れればverifyされる

    print(token)


if __name__ == "__main__":
    main()
