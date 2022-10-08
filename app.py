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
    app.run(host='0.0.0.0')
