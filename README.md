# フォルダ構成
- api: Flaskを利用した API Server
- client: React を利用した画面

# 起動方法
## API側
```shell
$ cd api/
$ pip install flask flask_cors flask_sqlalchemy marshmallow_sqlalchemy

$ flask run
```

## Client側
```shell
$ cd client/
$ npm install

$ npm start
```
