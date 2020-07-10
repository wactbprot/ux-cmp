from flask import Flask, request, send_from_directory, render_template

from flask_cors import CORS
import utils as utils
import trans as trans
from rio import Rio

config = utils.get_config_dict()

rio = Rio(config)
app = Flask(__name__)
CORS(app)

@app.route('/<mp_id>/<struct>/<idx>/state.html', methods=['GET'])
def state(mp_id, struct, idx):
    app.logger.debug('hit state.html')

    upper_page = render_template('html/upper.html')
    lower_page = render_template('html/lower.html')

    content = trans.state_html(rio, mp_id, struct, idx)
    print(content)
    return "{}{}{}".format(upper_page, content,lower_page)

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

    srv = config.get("server")
    host = srv.get("host")
    port = srv.get("port")

    app.run(host=host, port=port)
