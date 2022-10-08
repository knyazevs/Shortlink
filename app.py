import os

from flask import Flask

from db import mydatabase
from entities.LinkEntity import LinkEntity
from routes.ShortLinkRoutes import shortlink_page

app = Flask(__name__, static_url_path='', static_folder='web/static')
app.config['SECRET_KEY'] = "my secret"

mydatabase.connect()
mydatabase.create_tables([LinkEntity])


@app.teardown_appcontext
def close_connection(g):
    if mydatabase is not None:
        mydatabase.close()


app.register_blueprint(shortlink_page)

if __name__ == '__main__':
    host = os.getenv('HOST')
    if host is None:
        host = "127.0.0.1"
    port = os.getenv('PORT')
    if port is None:
        port = 80
    app.run(host=host, port=int(port), debug=False)
