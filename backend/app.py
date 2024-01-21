# app.py
from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer
import socket
from db_access.models import db
import db_access.db_service as service
import utils.utils_functions as ut
import utils.constants as C
from utils.log_service import get_logger
from loguru import logger

logger = get_logger()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tambola.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
# CORS(app, supports_credentials=True)

@logger.catch
@app.route('/generate/tickets', methods=['POST'])
def generate_tambola_tickets():
    try:
        logger.info("URL: {0}".format(request.url))
        # Check the request is JSON
        if not request.is_json:
            return ut.build_response(status=200, msg="Not json input")
        
        status, msg = ut.validate_parse_headers(request)

        if status != 200:
            return ut.build_response(status=status, msg=msg, data=request.data.decode(encoding='UTF-8'), success=False)

        status, msg = ut.validate_parse_input(
            request.json, [C.FIELDS.NUMBER_OF_SET])
        
        if status != 200:
            return ut.build_response(status=status, msg=msg, data=request.data.decode(encoding='UTF-8'), success=False)

        _setno = request.json[C.FIELDS.NUMBER_OF_SET]

        new_tickets = service.generate_n_tambola_sets(_setno)
        if new_tickets is None:
            return ut.build_response(msg="Error")

        new_tickets = {"tickets": new_tickets}
        return ut.build_response(msg="OK", data=new_tickets)
    except Exception as e:
        logger.error(f"Error in generate_tambola_tickets: {e}")
        return ut.build_response(msg="Error")

@logger.catch
@app.route('/get/all/tickets', methods=['GET'])
def get_tambola_tickets():
    try:
        logger.info("URL: {0}".format(request.url))
        _data = service.fetch_tambola_tickets()
        if _data is None:
            return ut.build_response(msg="Error")
        
        result = {"tickets": _data}
        response = ut.build_response(msg="OK", data=result)    
        return response
    except Exception as e:
        logger.error(f"Error in get_tambola_tickets: {e}")
        return ut.build_response(msg="Error")

@logger.catch
def main(flask_app=None):
    """
    the main function which runs the flask app
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    
    # ServiceHolder.init_app(flask_app)
    logger.info("Server Initiated ...")
    logger.info("Connect http://"+str(ip)+":"+str(C.GLOBAL.FLASK_PORT))

    WSGIServer((C.GLOBAL.FLASK_HOST, C.GLOBAL.FLASK_PORT),
               flask_app).serve_forever()
    # initialize database tables
    # ServiceHolder.__initialized = True
    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    main(app)
