from flask import Flask, request, send_from_directory, render_template
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

import utils as u
import trans as trans
from rio import Rio

config = u.get_config_dict()

rio = Rio(config)
app = Flask(__name__)
socketio = SocketIO(app)

CORS(app)

@app.route('/<mp_id>/<struct>/<idx>/state.html', methods=['GET'])
def state(mp_id, struct, idx):
    app.logger.debug('hit state.html')
    c = trans.container(rio, mp_id)
    d = trans.definitions(rio, mp_id)

    upper_page = render_template('html/upper.html',
                                 container=c,
                                 definitions=d)
    lower_page = render_template('html/lower.html')
    content = trans.state_html(rio, mp_id, struct, idx)
    
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

@socketio.on('connect')
def connect_web():
    callback = u.gen_callback(socketio, rio)
    rio.subscribe("*", callback)
    
    app.logger.debug('Web client connected: {}'.format(request.sid))

@socketio.on('disconnect')
def disconnect_web():
    app.logger.debug('Web client disconnected: {}'.format(request.sid))
    
if __name__ == '__main__':

    srv = config.get("server")
    host = srv.get("host")
    port = srv.get("port")

    socketio.run(app=app, host=host, port=port, debug=True)