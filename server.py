from flask import Flask, request, send_from_directory
from flask_cors import CORS
import utils as utils

app = Flask(__name__)
CORS(app)

@app.route('/<mp-id>/container/<idx>/state.html', methods=['GET'])
def validation():
    app.logger.debug('hit state.html')

    return "nil"

@app.route('/js/<fn>', methods=['GET'])
def js_folder(fn):
    app.logger.debug('hit js folder')
    return send_from_directory('static/js', fn)

@app.route('/css/<fn>', methods=['GET'])
def css_folder(fn):
    app.logger.debug('hit css folder')
    return send_from_directory('static/css', fn)

@app.route('/img/<fn>', methods=['GET'])
def logo_folder(fn):
    app.logger.debug('hit logo folder')
    return send_from_directory('static/img', fn)

if __name__ == '__main__':

    srv = utils.get_config_dict().get("server")
    host = srv.get("host")
    port = srv.get("port")

    app.run(host=host, port=port)
