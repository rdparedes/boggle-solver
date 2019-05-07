import os
import sys
import requests
from flask import jsonify, request, make_response, send_from_directory
from webargs import fields
from webargs.flaskparser import parser

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
os.environ.update({'ROOT_PATH': ROOT_PATH})
sys.path.append(os.path.join(ROOT_PATH, 'modules'))

import logger
from app import app
from app.boggle_solver import solve

LOG = logger.get_root_logger(os.environ.get(
    'ROOT_LOGGER', 'root'), filename=os.path.join(ROOT_PATH, 'output.log'))

# Port variable to run the server on.
PORT = os.environ.get('PORT')


@app.errorhandler(404)
def not_found(error):
    """ error handler """
    LOG.error(error)
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    """ static files serve """
    return send_from_directory('dist', 'index.html')


find_words_args= {"board": fields.List(fields.List(fields.Str(required=True)))}

@app.route('/find-words', methods=['POST'])
def find_words():
    args = parser.parse(find_words_args, request, error_status_code=400)
    board = args["board"]
    response = solve(board)
    return jsonify({ "data": response })


@app.route('/<path:path>')
def dist_proxy(path):
    """ dist folder serve """
    file_name = path.split('/')[-1]
    dir_name = os.path.join('dist', '/'.join(path.split('/')[:-1]))
    return send_from_directory(dir_name, file_name)

@app.route('/static/<subfolder>/<path:filename>')
def static_proxy(subfolder, filename):
    dir_name = os.path.join('dist','static', subfolder)
    return send_from_directory(dir_name, filename)


if __name__ == '__main__':
    LOG.info('running environment: %s', os.environ.get('ENV'))
    app.config['DEBUG'] = os.environ.get('ENV') == 'development' # Debug mode if development env
app.run(host='0.0.0.0', port=int(PORT)) # Run the app