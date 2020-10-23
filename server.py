import flask
from flask import render_template, json, request, Response
from datetime import datetime

app = flask.Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    current_time = datetime.now().isoformat()
    return render_template('go-owls.html', access_time=current_time)


#################################################################################
# Messages Handling
#################################################################################
# https://www.w3.org/Protocols/HTTP/HTRESP.html
# 200 - Success
# 400 - Bad Request
HTTP_CODE_SUCCESS = 200
HTTP_CODE_BAD_REQUEST = 400

class ApiResponseInterface:
    def __init__(self, success, message=None, data=None):
        self.success = success
        self.message = message
        self.payload = data

    def toJSON(self):
        return self.__dict__


# server-side in-memory collection
messages = []


@app.route('/messages/list', methods=['GET'])
def messages_list():
    json_response = json.dumps(messages)
    return Response(json_response, 200, mimetype='application/json')


@app.route('/messages/add', methods=['GET'])
def messages_add():
    # get the input parameter
    message = request.args.get('message', default=None, type=str)
    # todo: add good validation...
    has_validation_errors = message is None

    # response handling based on validation
    if has_validation_errors:
        # error response
        response_message = ApiResponseInterface(False, 'Invalid input data')
        json_response = json.dumps(response_message.toJSON())
        return Response(json_response, HTTP_CODE_BAD_REQUEST, mimetype='application/json')
    else:
        # create new message and add to collection
        new_message = {
            'message': message,
            'created_on': datetime.now().isoformat()
        }
        messages.append(new_message)

        # respond to the client
        response_message = ApiResponseInterface(True, 'Successfully created new message', new_message)
        json_response = json.dumps(response_message.toJSON())
        return Response(json_response, HTTP_CODE_SUCCESS, mimetype='application/json')


#################################################################################
# Run Application
#################################################################################
app.run(host="0.0.0.0")