from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def index():
    return "Rodando app flask em ambiente wsgi !"



if __name__ == '__main__':
    app.run(port = 8081, host = '127.0.0.1')