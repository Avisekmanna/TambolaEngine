
# stores all the required global constants
class GLOBAL():
    DEBUG = True
    # SECRET_KEY = "T@mb0lA$3Rv3r"
    FLASK_HOST = "0.0.0.0"
    FLASK_PORT = 9999

class MESSAGES():

    class SUCCESS():
        OK = {"code": 2000, "msg": "OK"}

    class ERROR():
        GENERIC = {"code": 1000, "msg": ""}
        SERVER = {"code": 1001, "msg": "Unknown Error! Please try later"}
        INVALID = {"code": 1003, "msg": "Invalid Data"}
        INVALID_CONTENT_TYPE = {
            "code": 1004, "msg": "Invalid content-type. Must be application/json"}

class FIELDS():
    NUMBER_OF_SET = "setno"

# stores all the required global variables which can be changed during runtime
class VARS():

    ROOT_DIR = ""
    LOG_DIR = "../"