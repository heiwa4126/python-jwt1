# python-jwd1

PythonでJWTのサンプル。

実行例
```bash
# HS256
./ex1.py

# RS256
./mkpare.sh
./ex2.py
```

出力を https://jwt.io/ にコピペし、
- ex1.py のほうは コード中の鍵を、
- ex2.py のほうは public_key_fileの中身を
`your-256-bit-secret` に貼り付けてverify

# 参考

- [PythonでPyJWTを使用し、JSON Web Token（JWT）を作成する | Men of Letters（メン・オブ・レターズ） – 論理的思考/業務改善/プログラミング](https://laboratory.kazuuu.net/using-pyjwt-in-python-to-create-a-json-web-token/)
- [PyJWT で JWT の生成と検証を行う - ymstmsys’s ブログ](https://ymstmsys.hatenablog.jp/entry/2022/02/05/144106)
