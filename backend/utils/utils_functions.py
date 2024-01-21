from flask import jsonify
from loguru import logger
import utils.constants as C
import sys

# Validate API Request Header
@logger.catch
def validate_parse_headers(request):
    """
    Validates headers content type. If not returns a proper error message.
    """
    status = 200
    message = ''

    _contenttype = request.headers.get('content-type')
    if not('application/json' in _contenttype ):   
        message = C.MESSAGES.ERROR.INVALID_CONTENT_TYPE
        status = 400

    return status, message

@logger.catch
def build_response(status=200,success = True, msg = "", data = {}):
    """
    Builds a json response in success, msg, data format
    """
    if msg is None or len(msg) == 0:
        msg = C.MESSAGES.SUCCESS.OK if success else C.MESSAGES.ERROR.SERVER
    
    if data is None:
        data = {}
    
    if(status != 200):
        success=False
    
    response = jsonify({"success": success,"msg": msg,"data": data})
    response.status_code = status
    # logger.info("\n Response :\n   Status : {0} \n     Msg : {1} \n     Data : {2} \n".format(success,msg,data))
    return response

# Validate API Request Input
@logger.catch
def validate_parse_input(content, keys):
    """
    Validates that the minimum set of keys that are needed to parse an alarm are there in the
    input. If not returns a proper error message.
    @returns status(int), message(string)
    """
    logger.info("\n Request : {0}".format(content))
    status = 200
    message = ''
    for key in keys:
        if key not in content:
            message = '{0} not found in input.'.format(key)
            status = 400
            break
    return status, message

